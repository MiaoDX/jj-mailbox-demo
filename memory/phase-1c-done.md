# Phase 1c: Profile Sync Script

## Status
✅ Completed 2026-04-15

## What
自动化脚本 `scripts/sync-profile.py`，将 agent profile 从 `agents/{agent}/profile.json` 同步到 `memory/snapshots/`。

## Usage
```bash
# 同步所有 agents
python3 scripts/sync-profile.py

# 同步单个 agent
python3 scripts/sync-profile.py gsd
```

## Output Format
Snapshot 文件包含原始 profile + `_sync` 元数据：
```json
{
  "name": "gsd",
  "full_name": "Get Stuff Done",
  ...
  "_sync": {
    "source": "agents/gsd/profile.json",
    "synced_at": "2026-04-15T04:47:58.852372+00:00",
    "version": "1.0"
  }
}
```

## Next
- Phase 2: 跨实例 Agent 消息总线（等待 MiaoDX 确认"不在群里的 claw"场景优先级）
