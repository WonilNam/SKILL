---
name: skill-creator
description: 高级 Skill 创建、审查和维护技能。用于新增、重写、拆分、审查或优化 Antigravity/Gemini/Codex/Copilot/Claude 风格的 SKILL.md；当用户要求创建 skill、改 skill、整理全局技能、补 metadata、优化触发条件、增加工具分支、压缩说明、补安全边界、对标 GitHub 热门 skill 或提升可复用性时使用。
---

# Skill Creator

目标：把 skill 写成可发现、可触发、可执行、可验证、可维护的能力包。高级 skill 不是长，而是判断分支清楚、工具边界明确、失败路径可处理。

## Required Anatomy

每个 `SKILL.md` 必须有 frontmatter：

```yaml
---
name: lowercase-hyphen-name
description: 说明 skill 做什么，以及哪些请求会触发它。触发词必须写在这里。
---
```

正文只在触发后加载，所以触发条件、适用场景和关键关键词必须放进 `description`。

## Quality Bar

高级 skill 至少包含：

- **Purpose**：一句话目标。
- **Routing**：何时使用哪条流程或工具。
- **Workflow**：可执行步骤，不是概念说明。
- **Tool Ladder**：优先工具、可选高级工具、无工具时降级方案。
- **Output Contract**：结构化输出格式。
- **Guardrails**：安全边界、确认门禁、禁止行为。
- **Validation**：如何确认 skill 自身和任务结果有效。

## Writing Rules

- 用 imperative/infinitive 风格，直接告诉 agent 怎么做。
- 保持短而密；删除模型已经知道的基础概念。
- 用真实命令、文件、格式和判断标准。
- 不声称不存在的能力，例如未安装索引、AST、浏览器、MCP 或 API。
- 操作型 skill 是允许的；搜索、执行、审查、规划都应写成可复用流程。
- 针对脆弱任务降低自由度：删除、Git、数据库、发布、凭据、外部命令必须有门禁。

## Upgrade Workflow

1. **Audit**：检查 frontmatter、触发描述、正文长度、工具依赖、安全边界和输出格式。
2. **Classify**：判断 skill 是 workflow、tool integration、domain knowledge、quality gate 还是 meta-skill。
3. **Sharpen Trigger**：把用户可能说的话写进 `description`，避免只写抽象能力名。
4. **Add Branches**：补常见场景分支，例如 simple/advanced、safe/destructive、search/AST/semantic。
5. **Add Degradation**：没有专用工具时写明怎么用通用工具完成。
6. **Add Examples Sparingly**：只放最能校准行为的示例命令或输出结构。
7. **Validate**：检查 YAML、名称、旧阻塞规则、危险命令边界、虚构工具声明。

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
- 正文有 Routing、Workflow、Output Contract、Guardrails。
- 高风险操作有确认门禁。
- 没有“必须停止”这类无谓打断；只有真实决策门禁才暂停。
- 没有虚构工具能力。
- 对外部分发时，补安装方式、依赖、兼容平台和 provenance/来源说明。
