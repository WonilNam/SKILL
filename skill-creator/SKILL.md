---
name: skill-creator
description: 创建、审查或改进 Agent Skill，包括 SKILL.md、触发描述和 supporting resources。当用户明确要求新增/优化 skill、拆分能力、对标社区实现或检查 Agent Skills 兼容性时使用；普通提示词和项目规则编辑不触发。
---

# Skill Creator

目标：用最少上下文提供 agent 原本不知道的决策信息，使 Skill 可发现、可执行、可验证且不越权。

## Principles

- `description` 只负责准确发现：写清做什么、何时用，并与相邻 Skill 区分。
- 正文只保留非显然流程、领域不变量、工具选择和安全边界；删除通用常识与重复政策。
- 条件化长内容放 `references/`，重复且脆弱的操作放 `scripts/`，输出复用材料放 `assets/`。
- Skill 不扩张用户任务或授权，不声称不存在的工具和外部能力。

## Workflow

1. 审查 frontmatter、触发范围、相邻 Skill、正文成本、资源引用和权限边界。
2. 用至少 3 个应触发、2 个不应触发的请求检查 description。
3. 删除重复内容，只为真实存在的模式保留路由和降级路径。
4. 仅当独立加载确实节省上下文时拆分 supporting resources。
5. 运行 `python skill-creator/scripts/validate_skills.py <skill-or-root>`，并用代表性任务检查行为。

## Quality

重点评估触发精度、决策价值、可执行性、上下文效率、安全与验证。不要机械要求 Tool Ladder、固定输出模板或同样的章节结构。

`name` 与目录名一致并使用 lowercase-hyphen；`description` 不超过 1024 字符。对外分发时再补兼容性、依赖、安装方式和来源信息。
