---
name: skill-creator
description: 创建、审查或改进 Agent Skill（SKILL.md 及其 scripts/references/assets）。当用户要求新增或优化 skill、调整触发描述、拆分技能、对标社区实现、补验证脚本或检查 Agent Skills 兼容性时使用；不要因普通提示词编辑而触发。
---

# Skill Creator

目标：用尽可能少的上下文提供模型原本不知道的决策信息，使 skill 可发现、可执行、可验证且不越权。

## Core Principles

- 假设 agent 已具备通用推理与编码能力，只保留会改变决策、工具选择或安全边界的内容。
- `description` 负责发现：写清“做什么、何时使用”，并用排除条件避免与相邻 skill 重叠；不要堆砌同义触发词。
- 正文负责执行：保留共享流程和关键不变量；条件化细节放到 `references/`，重复且脆弱的操作放到 `scripts/`。
- 用户授权边界高于 skill。skill 可以要求在危险动作前确认，但不能暗示已获得发布、删除、外部写入或凭据访问权限。

## Required Anatomy

每个 `SKILL.md` 必须有 frontmatter：

```yaml
---
name: lowercase-hyphen-name
description: 说明 skill 做什么，以及哪些请求会触发它。触发词必须写在这里。
---
```

正文只在触发后加载，所以触发条件、适用场景和关键关键词必须放进 `description`。

## Quality Model

按任务相关性评分，不要求每个 skill 机械地拥有同样章节：

- **触发精度 20**：描述可区分相邻能力，既不漏掉典型请求，也不吸引普通任务。
- **决策价值 20**：正文包含非显然知识、判断标准或领域不变量，而非通用建议。
- **可执行性 20**：工作流能落到真实工具、文件和失败分支。
- **上下文效率 15**：入口简洁，条件内容渐进加载，无重复说明。
- **安全与意图 15**：保留用户选择、权限和破坏性操作门禁。
- **验证性 10**：能校验结构，并通过真实任务或确定性脚本验证关键行为。

固定输出格式、Tool Ladder、Troubleshooting 或独立 Guardrails 章节仅在任务确实需要时添加。

## Writing Rules

- 用 imperative/infinitive 风格，直接告诉 agent 怎么做。
- 保持短而密；删除模型已经知道的基础概念。
- 用真实命令、文件、格式和判断标准。
- 不声称不存在的能力，例如未安装索引、AST、浏览器、MCP 或 API。
- 操作型 skill 是允许的；搜索、执行、审查、规划都应写成可复用流程。
- 针对脆弱任务降低自由度：删除、Git、数据库、发布、凭据、外部命令必须有门禁。

## Upgrade Workflow

1. **Audit**：检查 frontmatter、触发描述、正文长度、工具依赖、安全边界和输出格式。
2. **Classify**：判断它主要提供 workflow、tool integration、domain knowledge、quality gate 还是 meta-skill，并找出相邻技能。
3. **Test Trigger**：至少写 3 个应触发、2 个不应触发的真实请求，在修改前先判断误触发原因。
4. **Reduce**：删除模型已知常识、重复政策、装饰性术语和无行为影响的固定模板。
5. **Route**：只为真实存在的模式增加分支；工具不可用时提供可靠降级路径。
6. **Package**：需要复用或确定性时才增加 scripts/references/assets，并从 `SKILL.md` 明确说明何时读取或执行。
7. **Validate**：运行 `python skill-creator/scripts/validate_skills.py <skill-or-root>`；再用至少一个代表性任务检查真实行为，而不是只匹配标题或措辞。

## Split or Bundle

拆分 skill 的条件：

- 一个 skill 同时覆盖多个不相关领域。
- 正文超过维护舒适范围，且不同任务只需要其中一小部分。
- 有独立脚本、reference 或 assets 可以按需加载。

保留一个 skill 的条件：

- 它是一个连贯工作流。
- 任务通常会一起发生，例如搜索 + 读取上下文。
- 拆分会增加触发混乱。

## Resource Policy

- `scripts/`：重复、脆弱、需要确定性执行的逻辑。
- `references/`：长文档、规则手册、API 细节、示例库。
- `assets/`：输出会复用的模板、图片、字体、样板工程。
- 不创建 README、CHANGELOG、安装指南等无关文件，除非用户明确要求公开分发。

## Validation Checklist

- `name` 与目录名一致，使用 lowercase hyphen。
- `description` 包含功能、触发词和上下文。
- 正文包含完成任务所需的路由、流程和边界，但不强制固定章节。
- 高风险操作有确认门禁。
- 没有“必须停止”这类无谓打断；只有真实决策门禁才暂停。
- 没有虚构工具能力。
- supporting resource 能从入口按相对路径发现，没有孤立文件或未完成占位符。
- 对外分发时再补安装方式、依赖、兼容平台和 provenance/来源说明。

对于新增或大幅改写的复杂 skill，可在用户授权且多 agent 可用时做独立前向测试；普通小改动不必强制委派。
