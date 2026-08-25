---
name: code-intelligence
description: 基于代码、配置、测试和运行结果进行调试、代码审查或变更风险分析，定位可证明的根因与最小修复路径。当用户要求 debug/fix、review PR 或 diff、解释异常行为、检查逻辑/并发/权限/性能风险时使用；不用于纯样式审美反馈或没有代码证据的泛化架构讨论。
---

# Code Intelligence Skill

目标：做基于证据的工程判断。先收集代码、调用链、配置、测试和运行结果，再给结论；每个结论都要能回到文件、行号、日志或命令输出。

## Mode Routing

- **Debug**：用户给错误、异常行为、测试失败、线上症状或“帮我修”。
- **Review**：用户说 review、检查代码、看 PR、找风险。
- **Explain**：用户问某段逻辑怎么工作。
- **Risk Analysis**：用户准备重构、发布、迁移、改公共 API、改协议或数据库。
- **Auto**：先判断模式，再按对应流程执行。

## Evidence Loop

1. **Scope**：明确用户期望的行为和实际行为。
2. **Search**：用 file-search 找入口、调用点、配置、测试和相似实现。
3. **Read**：读取会影响行为的完整函数/类/组件，不只读命中行。
4. **Reproduce/Verify**：能运行就用 terminal-run 复现或验证。
5. **Trace**：从输入 -> 状态 -> 分支 -> 依赖 -> 输出/副作用建立因果链。
6. **Patch Strategy**：给最小、局部、符合现有架构的修复路径。
7. **Validation**：运行相关测试/构建/类型检查；不可运行时说明原因和替代验证。

先判断用户要“只分析”还是“直接修复”。默认修复请求包含实现与验证；review、解释、风险评估默认只读，不借机修改代码。

## Debug Playbook

- 先确认错误入口和最近一次稳定行为。
- 优先检查边界条件：null/undefined、空集合、权限、时区、编码、异步时序、并发、缓存、环境变量。
- 对状态机/协议/parser/framer：字段、状态、转移、测试、文档必须对齐；未知字段标 unknown。
- 对数据库/EF：检查 query shape、tracking、transaction、migration、nullable、索引和并发更新。
- 对前端：检查 props/state/store、computed/watch、API service、生命周期、loading/error/empty、移动端布局。
- 对微信小程序：检查 `setData` 粒度、生命周期、权限、BLE 异步回调、平台 API 支持。

## Review Playbook

输出 findings 优先，按严重度排序：

- **P0**：数据丢失、安全漏洞、无法启动、核心流程完全中断。
- **P1**：明确行为回归、错误结果、权限绕过、重要测试缺失。
- **P2**：边界问题、性能风险、可维护性问题、局部 UX 问题。
- **P3**：小问题、命名、注释、低风险清理。

每条 finding 必须包含：

- 位置：文件和行号。
- 影响：什么输入/场景会触发，用户或系统会看到什么。
- 证据：代码、测试、配置或运行结果。
- 建议：最小修复方向。

没有发现问题时，明确说“未发现阻塞问题”，并列出未验证范围。

## Architecture Judgment

只有在抽象能解决真实复杂度时才建议架构调整：

- 解决什么问题。
- 改变什么行为或边界。
- 引入什么取舍。
- 为什么适合当前项目规模。

不要为了展示模式而引入 DDD/CQRS/策略/事件；已有架构优先。

## Output Contracts

Debug：

```text
Root Cause:
Evidence:
- <path>:<line> — <fact>
Fix:
Validation:
Residual Risk:
```

Review：

```text
Findings:
- [P1] <title> — <path>:<line>
  Impact: <specific behavior>
  Evidence: <fact>
  Fix: <minimal change>
Open Questions:
Summary:
Tests:
```

模板用于保证 finding 可执行，不要求在没有内容时保留所有空字段。

## Guardrails

- 不把猜测写成事实。
- 不用大重构替代根因定位。
- 不忽略测试失败中的第一条关键错误。
- 不在 review 中列没有行为影响的个人偏好。
- 修复后重新读取实际 diff，确认没有把用户的未提交改动或无关格式变化混入结果。
