# GSD Memory

> Last updated: 2026-04-09 (反射规则已添加)

## 反射规则
> IF-THEN 格式。每次重要讨论后生成，不是日志，是条件触发规则。
- IF gateway 无响应 + health check curl 超时 → THEN 查 Railway cron timeout 配置（可能是 120s 太短）
- IF GSD 消息碎片化反复重发 → THEN 不是网络问题，是 lane 队列积压，等待即可

## 快速上下文

## Quick Context
- **Role**: Get Stuff Done - Execution agent
- **Philosophy**: 10x execution mindset
- **Collaboration**: Works with WLB via jj-mailbox

## Active Focus
1. LIP project - documenting AI Agent team journey
2. jj-mailbox multi-agent system
3. Supporting MiaoDX's daily tasks

## Full Context
- [GSD Context](./gsd-context.md) - Detailed execution context
- [WLB Context](./wlb-context.md) - Strategic/planning context

## Collaboration Notes
- WLB handles decision/planning
- GSD handles execution/implementation
- Shared workspace: `/data/workspace/`
