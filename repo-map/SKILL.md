---
name: repo-map
description: 建立代码库或单个功能的证据化地图，识别技术栈、入口、模块职责、依赖方向、测试与构建边界。当用户询问项目结构、数据流、模块关系、架构边界，或多模块改动前需要确定影响范围时使用；不要为只涉及一个已知文件的小改动加载全仓库地图。
---

# Repo Map Skill

目标：在不淹没上下文的前提下，建立足够准确的仓库地图，指导后续搜索、规划、调试和重构。

## Mapping Depth

按任务选择深度：

- **Scan**：30 秒内看顶层目录、配置文件、入口和测试目录。
- **Feature Map**：围绕一个功能找路由/API、状态、领域对象、服务、测试和文档。
- **Architecture Map**：分析项目引用、模块边界、依赖方向、数据流和风险。
- **Change Map**：为即将修改的任务列出会受影响的文件和验证点。

## Workflow

1. **Inventory**：用 `rg --files` 或目录列表识别源码、测试、文档、配置、脚本、生成目录。
2. **Stack Evidence**：根据 `*.sln`、`*.csproj`、`package.json`、workspace 文件、`vite.config.*`、`app.json`、`go.mod`、`Cargo.toml` 等确认技术栈。
3. **Entry Points**：定位运行入口、路由入口、DI/bootstrapping、测试入口、构建入口和小程序页面入口。
4. **Boundaries**：按项目引用、命名空间、目录、feature/module/layer、路由和数据访问边界归纳职责。
5. **Dependency Direction**：读取真实 import/export、project reference、DI 注册、router/store/API service、EF config，而不是只看目录名。
6. **Risk Notes**：标出循环依赖、跨层调用、重复实现、生成文件、缺测试区域和未知点。

## Evidence Ranking

1. 构建/项目配置：solution、project reference、workspace、package scripts。
2. 运行时注册：DI、router、middleware、store、plugin、app/page 注册。
3. 源码引用：import/export、namespace、using、API service、repository。
4. 测试：覆盖边界和行为意图。
5. 文档：解释意图，但必须和代码核对。
6. 目录命名：只能作为推断，不能单独作为事实。

## Stack-Specific Checks

- **.NET/Clean Architecture**：API/Application/Domain/Infrastructure 分层、CQRS handler、repository interface/implementation、EF configuration、migration、DI 注册、test project。
- **Vue/Vite**：`src/main.*`、router、Pinia、views、components、composables、services/api、env、vite alias。
- **微信小程序**：`app.json`、pages、components、分包、utils、BLE/protocol/parser/framer、权限和生命周期。
- **Monorepo**：workspace roots、package graph、shared packages、build pipeline、cross-package imports。

## Result Shape

当用户明确要仓库地图时使用完整结构；作为规划前置步骤时只返回与当前改动有关的模块、依赖和风险：

```text
Map Depth: <scan|feature|architecture|change>
Tech Stack:
- <evidence-backed stack item> (<file>)
Entry Points:
- <path>:<line> — <runtime/build/test/router/etc>
Module Map:
- <module> — <responsibility> — <key files>
Dependency Direction:
- <from> -> <to> (<evidence>)
Change/Risk Notes:
- <risk, unknown, or follow-up search>
```

## Guardrails

- 不生成虚构 AST 图、调用图或 symbol index。
- 如果没有依赖分析工具，只能说“根据配置和 import 推断”。
- 不把 vendor、dist、build、coverage、cache 当作架构事实来源。
- 发现上下文冲突时直接标出冲突，并说明需要哪类证据解决。
- 地图只做到足以支持当前问题；不要遍历无关模块来追求“完整”。
