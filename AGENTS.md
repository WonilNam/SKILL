# 全局 Codex 指令

## 主要用途

我主要使用 Codex 做软件开发相关工作：功能实现、调试、重构、代码审查、测试、文档、架构设计和发布准备。

请把我当作有经验的开发者。除非我主动要求，不要解释基础概念。

## 核心技术栈

优先考虑以下技术栈和模式：

- .NET 8 / C# / ASP.NET Core
- Entity Framework Core
- DDD / Clean Architecture / CQRS / 分层架构
- 微信小程序原生开发
- Vue 3 / Vite / TypeScript
- 前端工程化、组件设计、状态管理、API 服务层
- HTML / CSS / JavaScript / TypeScript

在引入新的库或模式前，始终优先遵循现有项目的技术栈、结构、命名和架构。

## 默认编码行为

当我要求修复、功能、重构、测试、文档或清理时，直接实现，除非我明确说“only analyze”“do not edit”或“先别改代码”。

编辑前：

- 先检查相关代码。
- 检查当前约定。
- 保持改动范围聚焦当前任务。
- 不重写无关模块。

编辑后：

- 在可行时运行已有测试或类型检查。
- 汇报改了什么、验证了什么。
- 如果无法运行测试，说明原因。

## 架构偏好

我偏好现代、可维护的架构：

- DDD
- Clean Architecture
- 领域模型
- 应用服务
- 仓储接口
- 状态机
- 策略模式
- 领域事件
- CQRS
- 明确的模块边界和职责

不要为了显得高级而过度设计。只有当抽象能解决真实复杂度、减少有意义的重复、澄清边界或支持合理扩展时，才引入抽象。

对于小项目，保持实现简单；如果有价值，可以说明一个合理的未来演进路径。

提出架构建议时，说明：

- 这个抽象解决什么问题
- 它影响什么行为
- 它引入什么取舍
- 为什么适合当前项目规模

## .NET 8 偏好

优先使用现代 C# 和 .NET 实践：

- Nullable reference types
- Records / record structs，在合适时使用
- Primary constructors，在能提升清晰度时使用
- Pattern matching
- Async/await
- Dependency injection
- Options pattern
- 清晰的验证层，例如项目已使用 FluentValidation 时沿用
- EF Core 配置保持显式、可维护
- 对业务失败，在合适时使用 Result/Error 模型

对于 DDD 代码，清晰区分：

- Entity
- Value Object
- Aggregate Root
- Domain Service
- Application Service
- Repository Interface
- Infrastructure Implementation

## 微信小程序偏好

开发微信小程序时，考虑：

- 小程序运行时限制
- 微信异步 API
- BLE、网络、权限、生命周期行为
- 高效使用 `setData`
- WXML / WXSS / JS 分离
- 不使用小程序不支持的浏览器 API
- 测试页面只保留有用控件

对于 BLE、设备协议、parser/framer 工作：

- 协议字段必须在代码、文档和测试中保持一致。
- 不要编造未知协议细节。
- 优先以旧协议文件、当前 parser/framer 代码和测试作为证据。
- 如果字段无法从代码确认，将其标记为 unknown，或添加调试日志用于真机确认。

## Vue 3 / 前端偏好

优先使用：

- Composition API
- `<script setup>`
- TypeScript
- Vite
- Pinia
- Vue Router
- 可复用组件
- Composables
- 清晰的 API 服务层

不要把所有逻辑堆进一个大组件。保持状态、副作用、API 调用和渲染职责分离。

## UI / 视觉设计偏好

我喜欢高级、未来感、精致的设计，尤其是：

- 粒子效果
- 光效
- Glassmorphism
- 高级动效
- 3D / WebGL / Three.js
- 深色高级主题
- 精致渐变、辉光、流体、动态背景

设计仍必须服务功能。不要在我要求 app、工具、dashboard 或页面时做空洞的营销壳。

对于高级视觉：

- 保持文字可读。
- 保持交互清晰。
- 避免移动端布局破坏。
- 避免让页面变慢的效果。
- 当效果重要时，优先使用真实 Canvas/WebGL/Three.js 动效。

## 计划规则

当任务涉及以下情况时，先写一个简短计划：

- 多文件改动
- 架构改动
- 协议、状态机或领域模型改动
- 数据库 schema 改动
- 前后端集成
- 公共 API 或文档改动
- 文件删除或目录迁移
- 需求不清晰或风险需要拆解

计划必须包含：

- 可能改动的模块/文件
- 为什么这个方案合适
- 可能影响的行为
- 验证策略

对于小改动，例如重命名一个字段、改一条注释或删除一个按钮，不需要正式计划。

如果需求清晰，写完计划后直接继续实现，不需要等待确认。只有当确实需要业务决策或破坏性选择时才提问。

## Git 规则

非小改动前，先检查 `git status`。

不要：

- 覆盖、还原或删除我的未提交改动，除非我明确要求。
- 使用 `git reset --hard`。
- 使用 `git checkout -- .`。
- 未经明确指令 rebase、force-push 或改写历史。
- 把无关文件混进一个 commit。
- 提交临时文件、构建产物、日志或 IDE 缓存。

删除文件前，确认删除与当前任务直接相关。

提交前：

- 检查 `git diff`。
- 检查 `git status`。
- 在可行时运行测试/类型检查。
- 确认文档、测试和示例同步。
- 使用清晰的提交信息。

提交信息格式：

```text
Verb + specific object + purpose
```

示例：

```text
Refine H30 parser state transitions
Align SDK guide with public API
Fix WiFi scan SSID parsing
Remove obsolete test page controls
```

只有当我明确要求 submit、publish、push、release 或 commit 时，才运行 `git commit` 或 `git push`。

推送前：

- 确认当前分支。
- 确认远程仓库。
- 如果 push 失败，不要 force push，先解释失败原因。
- 如果需要新分支，默认使用 `codex/` 前缀。

## 文档规则

文档必须与代码一致。

更新文档时：

- 对照代码验证 API 名称、字段名、返回值和示例。
- 当 Markdown GUIDE 和 HTML GUIDE 同时存在时，保持一致。
- 从文档、测试页面和示例中移除废弃接口。
- 不要把猜测的协议细节写成事实。
- 将未知协议字段标记为待确认，或添加调试日志。
