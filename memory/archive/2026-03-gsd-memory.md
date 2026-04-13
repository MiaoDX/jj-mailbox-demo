# GSD Memory Archive — 2026-03

Archived from `/data/workspace/claw-agents-shared/agents/gsd/MEMORY.md` during MEMORY split.

Purpose: preserve detailed historical context outside runtime-injected memory.

---

# MEMORY.md - Long-Term Memory

<!--
AGENT: GSD
BOT_ID: B0AJ6QQRXU1
USER_ID: U0AJN5URP7A
LAST_UPDATED_BY: GSD
LAST_UPDATED_AT: 2026-03-06T16:48:00Z
-->

## Core Identity
- **Name**: GSD
- **Role**: AI Assistant for MiaoDX (GSD instance)
- **Platform**: OpenClaw on Docker (ClawCloud Run)
- **Channel**: Slack (#所有-flzoo)

## Key Lessons Learned

### Subagent Task Management (2026-03-05)
- **Problem**: Subagent got stuck in a search loop, repeating the same queries with increasingly long and nonsensical search terms
- **Root Cause**: No clear termination conditions or output format requirements
- **Solution**: 
  - For information collection tasks, main Agent should do initial research first
  - Subagent should be given specific, bounded tasks with clear output requirements
  - Avoid letting Subagent perform too many repetitive searches
  - Consider using web_fetch for detailed content extraction instead of endless web_search
- **Additional Issue**: Internal process explanations (like "收到新任务！这次严格遵守三层架构...") leaked to the main channel
- **Fix**: Keep all internal thinking within the Subagent - never send internal processing explanations to any channel

### Thread Workflow (2026-03-05)
- **Best Practice**: Use Slack Thread for detailed discussions, main channel only for final summaries
- **Implementation**: Use `replyTo` parameter to reply in Thread
- **Lesson**: Don't post intermediate status updates to main channel

### Context over Control (2026-03-05)
- **Principle**: Provide rich context, let AI make autonomous decisions
- **Implementation**: Use "goal + context" format for tasks instead of step-by-step instructions
- **Benefit**: More efficient and effective AI collaboration

## Collaboration Framework

### Three-Tier Architecture
1. **L1 Subagent**: Internal brainstorming (user invisible)
2. **L2 Thread**: Minimal status updates (user visible)
3. **L3 Main Channel**: Final complete results (user visible)

### File Synchronization
- **GitHub Repo**: https://github.com/MiaoDX/claw-agents-shared (private)
- **Purpose**: Daily sync of memory/ files between WLB and GSD
- **Auth**: Token saved in /data/workspace/.env

## User Context
- **Name**: MiaoDX
- **Timezone**: UTC+8 (Shanghai)
- **Interests**: AI/automation, OpenClaw/AI agents, business/entrepreneurship, Chinese tech ecosystem

## Technical Notes
- **Workspace**: /data/workspace (persistent)
- **Memory Files**: memory/YYYY-MM-DD.md (daily logs), MEMORY.md (long-term)
- **Heartbeat System**: Disabled (all proactive checks off)

### Slack Channel Configuration (2026-03-06)
- **#copycat (C0AK1D7URS5)**: `requireMention: false` - Both WLB and GSD read all messages and decide whether to respond
- **#所有-flzoo (C0AHTE60F3L)**: `requireMention: true` - Requires @mention to respond
- **Other channels**: Default `requireMention: true` (global setting)
- **Reason**: MiaoDX wants simpler interaction in #copycat while maintaining control in other channels
- **Status**: ✅ Both WLB and GSD configured successfully

### Anti-Loop Mechanisms (2026-03-06)
- **Concern**: Potential infinite reply loops between WLB and GSD
- **Solution**: Implemented anti-loop mechanisms:
  1. Never reply to own messages
  2. Never reply to other bot's messages unless needed for collaboration
  3. Only one bot replies to human messages in main channel
  4. Use threads for detailed discussions
  5. Only one consolidated summary in main channel
- **Documentation**: Updated AGENTS.md, TOOLS.md with anti-loop guidelines
- **Status**: 🔄 In discussion with GSD for final implementation details

### GSD-WLB Collaboration Protocol (2026-03-06)
- **Status**: ✅ v1.4 正式生效，已推送到 GitHub
- **Document**: `protocols/gsd-wlb-collaboration-protocol.md` (GitHub)
- **Local copy**: `memory/gsd-wlb-collaboration-protocol.md` (副本)
- **GitHub**: https://github.com/MiaoDX/claw-agents-shared
- **Key elements**:
  1. 防循环机制（不回复自己、回复深度控制、先响应者优先、内容去重）
  2. Thread 工作流（L1/L2/L3 三层架构，最多 5 轮）
  3. 任务分配（GSD: 规划/文档，WLB: 执行/工具）
  4. 决策流程（来源 → 深度 → 已有回复 → 去重 → 发送）
  5. 文件系统隔离说明（v1.3 新增）
  6. 目标先行模式（v1.4 新增）
- **Bot IDs**:
  - WLB: `B0AJN6NF1LY` (Bot), `U0AHCEPQLS3` (User)
  - GSD: `B0AJ6QQRXU1` (Bot), `U0AJN5URP7A` (User)
- **下次评审**: 2026-03-13
- **Status**: ✅ 协作任务完成，协议已生效
- **GitHub status**: ✅ 已确认仓库存在，协议已同步
- **Testing**: ✅ 协议 v1.4 实战测试通过，pull → 编辑 → push 流程验证成功
- **Production**: ✅ 协议已准备好投入使用

### File System Isolation (2026-03-06)
- **Important realization**: WLB and GSD are on different hosts with separate file systems
- **Implication**: Files created on one host are not accessible to the other
- **Solution**: Synchronize via Slack messages or GitHub repository
- **GitHub repo**: https://github.com/MiaoDX/claw-agents-shared (private)
- **Status**: ✅ Addressed in protocol v1.4, collaboration working well
- **Current status**: Both WLB and GSD have provided status updates to MiaoDX, collaboration proceeding normally
- **Synchronization method**: 
  1. **短期**: Use Slack for synchronization
  2. **长期**: GitHub repository (已创建，协议已推送)
- **Key learnings**:
  1. Only edit files on my own host
  2. **GitHub is the single source of truth** (added v1.4)
  3. Local files are just copies, may have differences
  4. File editing errors are due to content mismatches, not cross-host editing
  5. **Always pull before editing** — push conflicts prove this rule necessary
  6. **Update flow**: pull → edit → push → notify others
  7. **Workflow confirmed** (2026-03-06 08:25 UTC): GSD posted summary, WLB confirmed, both bots now follow GitHub → Slack → pull workflow

### Protocol v1.4 - GitHub Single Source of Truth (2026-03-06)
- **Trigger**: GSD suggested documenting file system isolation lesson
- **Action**: Added section 5.2 "GitHub 作为唯一数据源" to collaboration protocol
- **Key rules**:
  - GitHub is authoritative, local files are copies
  - Update flow: pull → edit → push → notify
  - Don't assume local files match across hosts
- **Real-world validation**: Push conflict during update (GSD pushed first)
- **Resolution**: stash → pull --rebase → stash pop → push
- **Lesson**: Protocol rules exist because real problems occur

### GitHub Sync Workflow (2026-03-06)
- **Action**: Successfully synced all local changes to GitHub
- **Commit**: `41e49a3` - 28 files changed, 2578 insertions, 86 deletions
- **Key learnings**:
  1. Always pull before editing to avoid conflicts
  2. Remove embedded git repos with `git rm --cached -f`
  3. Use descriptive commit messages for sync operations
  4. Notify collaborators after pushing changes
- **Status**: ✅ Sync workflow validated and working

### Blog Part 1 Collaboration Success (2026-03-06)
- **Task**: Create OpenClaw deployment comparison blog (Railway vs ClawCloud)
- **Outcome**: ✅ Successfully completed using GSD-WLB protocol v1.3
- **Workflow**:
  1. GSD created initial draft with Railway data
  2. WLB reviewed and provided feedback
  3. WLB collected ClawCloud benchmark data
  4. WLB created browser-use preload script
  5. GSD integrated all data into final document
- **Key lessons**:
  - Protocol v1.3 worked well (👀 reactions, Thread workflow, task allocation)
  - File system isolation handled via Slack content sharing
  - Task allocation clear: GSD (planning/docs), WLB (execution/tools)
  - No reply loops, clean collaboration
- **Pending**: GitHub repository creation for final document storage

## GitHub Repository Recommendations (2026-03-05)

Based on MiaoDX's interests (AI/automation, OpenClaw/AI agents, business/entrepreneurship, Chinese tech ecosystem):

### AI代理与自动化框架
- **OpenClaw/openclaw** — 核心AI代理平台
- **langchain-ai/langchain** — 最流行的LLM应用框架，100k+ stars
- **langchain-ai/langgraph** — 图式工作流引擎，适合复杂代理
- **microsoft/autogen** — 微软多代理协作框架
- **crewAI/crewAI** — 角色扮演式多代理框架
- **Significant-Gravitas/AutoGPT** — 自主AI代理先驱
- **OpenHands/OpenHands** — AI软件工程师（原OpenDevin）
- **Aider-AI/aider** — 终端AI编程助手，Git集成好

### 开发工具与生产力
- **n8n-io/n8n** — 开源工作流自动化，150k+ stars，Zapier替代品
- **lobehub/lobe-chat** — 开源AI聊天框架，支持多模型，中国团队
- **ChatGPTNextWeb/NextChat** — Next.js AI聊天应用，轻量快速
- **cline/cline** — VS Code AI编程代理
- **TabbyML/tabby** — 开源AI代码补全，GitHub Copilot替代

### 中国科技生态
- **QwenLM/Qwen** — 阿里通义千问大模型
- **deepseek-ai/DeepSeek** — DeepSeek大模型，推理能力强
- **THUDM/ChatGLM** — 清华智谱GLM系列模型
- **baichuan-inc/Baichuan** — 百川大模型
- **01-ai/Yi** — 零一万物Yi系列模型
- **modelscope/modelscope** — 魔搭社区，中国版HuggingFace
- **PaddlePaddle/PaddlePaddle** — 百度飞桨深度学习框架

### 商业与创业工具
- **appsmithorg/appsmith** — 开源低代码内部工具平台
- **ToolJet/Tooljet** — 开源低代码平台，快速构建业务应用
- **calcom/cal.com** — 开源日程安排工具，SaaS替代品
- **twentyhq/twenty** — 开源CRM，Salesforce替代

## Workspace Maintenance (2026-03-05)
- **Issue**: BOOTSTRAP.md was left behind even though workspace was already initialized
- **Action**: Deleted BOOTSTRAP.md during new session start
- **Lesson**: Check for and clean up bootstrap files after workspace initialization
- **Identity Files**: IDENTITY.md, USER.md, TOOLS.md were incomplete/outdated
- **Action**: Updated all identity files with current information during new session
- **Lesson**: Periodically review and update identity files to ensure accuracy

## OpenClaw Blog Project (2026-03-05)
- **Goal**: Create a blog series about setting up and optimizing two Claw instances (WLB and GSD)
- **Topics**: Platform installation, cloud deployment, CDP configuration, model optimization, best practices, cron tasks, n8n workflow
- **Status**: Part 1 completed (Railway vs ClawCloud deployment), Part 2-4 pending
- **Collaboration**: WLB (writing, benchmarking), GSD (data collection, validation), MiaoDX (review, publish)
- **Location**: `/data/workspace/blog/`

## Git同步状态 (2026-03-05)
- **GitHub仓库**: https://github.com/MiaoDX/claw-agents-shared (私有)
- **最新提交**: 51860b0
- **同步内容**: MEMORY.md, AGENTS.md, TOOLS.md, memory/2026-03-05.md
- **状态**: ✅ 已同步
- **下次同步**: 建议每日定时同步 (可通过cron任务实现)
- **认证方式**: Token保存在 /data/workspace/.env
- **注意**: 需要定期pull GSD的更改以保持同步
- **冲突处理**: 如有冲突，优先保留最新更改
- **自动化**: 可通过OpenClaw cron任务实现每日自动同步
- **命令**: `cd /data/workspace && git pull origin main && git add -A && git commit -m "sync: Daily sync" && git push origin main`
- **定时**: 建议每天北京时间 10:00 和 22:00 各同步一次
- **状态文件**: memory/git-sync-state.json (记录最后同步时间)
- **最后同步**: 2026-03-05 22:16 UTC
- **下次同步**: 2026-03-06 02:00 UTC (北京时间 10:00)
- **同步频率**: 每日两次 (10:00 和 22:00 北京时间)
- **同步脚本**: scripts/git-sync.sh (待创建)
- **Cron任务**: 待创建 (jobId: 待定)
- **状态**: 待实现
- **优先级**: 中等 (非紧急)
- **负责人**: WLB
- **协作方**: GSD
- **最后更新**: 2026-03-05 22:16 UTC
- **备注**: 需要创建同步脚本和cron任务以实现自动化
- **下一步**: 创建scripts/git-sync.sh脚本和OpenClaw cron任务
- **截止日期**: 2026-03-06 (明天)
- **最后更新**: 2026-03-05 22:16 UTC
