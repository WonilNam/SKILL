---
name: plan
description: 高级软件开发规划与变更设计技能。用于多文件改动、架构调整、协议/状态机/领域模型变更、数据库 schema、前后端集成、公共 API、文档同步、文件删除、目录迁移、发布准备和高风险任务拆解；当影响范围不清晰、需要验证策略、存在业务取舍或需要先设计再实现时使用。
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

## Output Contract

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
