---
name: plan
description: 为多文件或高风险软件变更制定可执行计划，覆盖真实影响范围、设计取舍、行为变化、决策门禁和验证策略。当任务涉及架构、协议/状态机、数据库、前后端契约、公共 API、迁移、删除或发布准备时使用；单文件低风险修改不需要正式计划。
---

# Plan Skill

目标：在动手前把目标、影响范围、方案、风险和验证路径说清楚，然后在需求清晰时继续实现。计划是执行工具，不是暂停仪式。

## Complexity Routing

- **Tiny**：单行文案、注释、明显 typo、小样式。直接改，不写正式计划。
- **Focused**：单模块、小范围 bug、单组件。简短说明思路后执行。
- **High**：多文件、跨层、公共 API、状态机、协议、数据库、架构边界。先写计划，再执行。
- **Full**：迁移、重构、发布、目录移动、删除、跨系统集成。先建立 repo map 和验证矩阵。

## Planning Workflow

1. **Goal**：一句话定义目标行为，不只描述代码动作。
2. **Current Evidence**：列出已读取的关键文件/配置/测试；未知时先搜索。
3. **Impact Radius**：新增、修改、删除、受影响测试和文档。
4. **Design Choice**：说明为什么这个方案符合现有架构，避免过度设计。
5. **Behavioral Impact**：说明会改变哪些输入、输出、状态、权限、数据或 UI。
6. **Validation Matrix**：列出要跑的测试、构建、类型检查、手工验证和无法验证部分。
7. **Rollback/Containment**：高风险任务说明如何限制影响或回退。

## Decision Gates

需要用户确认后再继续：

- 删除数据或非临时文件。
- 数据库破坏性迁移、公共 API 破坏性变更、协议字段不确定。
- 改写 Git 历史、force push、发布、生产环境操作。
- 业务规则缺失且无法从代码/文档推断。
- 多个方案会明显影响产品行为、成本、性能或维护边界。

不需要确认：

- 需求清晰、影响范围可控、可通过测试验证的普通实现。
- 遵循现有模式的小重构。
- 文档与代码同步、测试补齐、明显 bug 修复。

## Plan Shape

```text
Plan Level: <tiny|focused|high|full>
Goal:
Evidence:
- <path>:<line> — <why it matters>
Impact Radius:
- Add:
- Modify:
- Delete:
Approach:
Behavior Changes:
Validation:
Gates:
- <none|required decision>
```

## Execution Rules

- 计划里的路径必须来自真实搜索或已读文件。
- 执行中发现计划不成立时，更新计划并说明原因。
- 不列无意义步骤，不输出大段代码。
- 计划后能执行就继续执行，除非命中 Decision Gates。
- 前后端集成时，必须严格核对并遵循大小写转换契约（如 .NET 的 PascalCase 与前端/小程序的 camelCase 的映射转换），防止字段因大小写不一致导致的反序列化失败。
- 计划粒度与风险成正比；没有删除项或决策门禁时省略空标题，不为填模板制造步骤。
