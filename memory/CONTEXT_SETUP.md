# Context Analysis Setup

## Overview
自动分析 Slack 群聊并生成精简的 agent context 文件，减少 token 使用量。

## Files

### Scripts
- `scripts/context-analyze.sh` - 主分析脚本
  - 为 WLB 和 GSD 生成各自的 context 文件
  - 分析所有群聊的活动水平
  - 更新主 MEMORY.md

### Generated Files
- `memory/MEMORY.md` - 主内存文件（精简版）
- `memory/wlb-context.md` - WLB 详细上下文
- `memory/gsd-context.md` - GSD 详细上下文
- `logs/context-analysis.log` - 运行日志

## Usage

### 手动运行
```bash
cd /data/workspace
./scripts/context-analyze.sh
```

### 参数
```bash
# 生成所有 context
./scripts/context-analyze.sh

# 仅生成 WLB context
./scripts/context-analyze.sh --agent wlb

# 仅生成 GSD context
./scripts/context-analyze.sh --agent gsd
```

## Channel Analysis

脚本会分析 `channels-T0AJ6BR0BFB.txt` 中列出的所有频道：

| 活动水平 | 消息数 | 说明 |
|---------|-------|------|
| High | > 50 | 活跃频道，context 可靠 ✅ |
| Medium | 10-50 | 一般活动 |
| Low | < 10 | 低活动，context 可能不完整 ⚠️ |

## Cron Job (待配置)

由于当前环境没有 cron，使用以下替代方案：

1. **OpenClaw HEARTBEAT** - 已更新 HEARTBEAT.md 添加每日检查任务
2. **手动触发** - 需要时手动运行脚本
3. **外部调度** - 可通过外部 cron 调用

### 外部 Cron 配置示例
```bash
# 添加到系统 crontab
0 2 * * * cd /data/workspace && bash scripts/context-analyze.sh >> logs/cron-context.log 2>&1
```

## Results

### Token 优化效果
- **Before**: MEMORY.md ~30,800 tokens
- **After**: MEMORY.md ~905 tokens
- **Reduction**: 97%

### System Prompt
- **Before**: ~50K tokens
- **After**: ~22K tokens

## Notes

- 低活动频道的 context 可能不完整
- 建议优先关注高活动频道的信息
- 每日自动更新确保 context 新鲜度
