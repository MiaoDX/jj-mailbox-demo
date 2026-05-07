#!/usr/bin/env python3
"""
jj-mailbox profile sync script (Phase 1c)

Syncs agent profiles from agents/{agent}/profile.json to memory/snapshots/
Usage: python3 scripts/sync-profile.py [agent_name]
"""

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

# Project root (script is in scripts/)
PROJECT_ROOT = Path(__file__).parent.parent
AGENTS_DIR = PROJECT_ROOT / "agents"
SNAPSHOTS_DIR = PROJECT_ROOT / "memory" / "snapshots"

def sync_agent_profile(agent_name: str) -> bool:
    """Sync a single agent's profile to snapshot."""
    source = AGENTS_DIR / agent_name / "profile.json"
    if not source.exists():
        print(f"❌ Profile not found: {source}")
        return False
    
    # Ensure snapshots dir exists
    SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Read source profile
    with open(source, 'r') as f:
        profile = json.load(f)
    
    # Add sync metadata
    snapshot = {
        **profile,
        "_sync": {
            "source": str(source.relative_to(PROJECT_ROOT)),
            "synced_at": datetime.now(timezone.utc).isoformat(),
            "version": "1.0"
        }
    }
    
    # Write snapshot
    target = SNAPSHOTS_DIR / f"{agent_name}-profile.snapshot.json"
    with open(target, 'w') as f:
        json.dump(snapshot, f, indent=2, ensure_ascii=False)
    
    print(f"✅ {agent_name}: {source} → {target}")
    return True

def sync_all_profiles() -> tuple[int, int]:
    """Sync all agent profiles. Returns (success_count, total_count)."""
    if not AGENTS_DIR.exists():
        print(f"❌ Agents directory not found: {AGENTS_DIR}")
        return 0, 0
    
    agents = [d.name for d in AGENTS_DIR.iterdir() if d.is_dir()]
    success = sum(1 for agent in agents if sync_agent_profile(agent))
    return success, len(agents)

def main():
    if len(sys.argv) > 1:
        # Sync specific agent
        agent = sys.argv[1]
        success = sync_agent_profile(agent)
        sys.exit(0 if success else 1)
    else:
        # Sync all agents
        success, total = sync_all_profiles()
        print(f"\nSynced {success}/{total} profiles")
        sys.exit(0 if success == total else 1)

if __name__ == "__main__":
    main()
