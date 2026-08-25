---
name: api-contract
description: 设计、修改或核对跨进程契约，覆盖 HTTP API、DTO、事件/消息、序列化命名、错误模型、兼容性和客户端映射。当任务涉及 ASP.NET Core 与 Vue/微信小程序集成、OpenAPI、公共请求/响应或消息字段变化、反序列化问题时使用；不用于纯内部方法签名调整。
---

# API Contract

目标：让生产者、消费者、文档和测试对同一份可观察契约达成一致，并显式处理兼容性。

## Evidence First

从真实 endpoint、DTO、serializer 配置、OpenAPI、客户端 service/types、调用页面和契约测试建立字段矩阵。文档只能解释意图，不能覆盖运行时代码事实。

至少核对：

- 路径、HTTP method、认证/权限、content type。
- 请求与响应字段名、大小写、类型、nullable、默认值、枚举和日期/时区格式。
- 成功状态码、业务失败模型、验证错误、分页与幂等语义。
- .NET `PascalCase` 到 JSON/TypeScript/小程序 `camelCase` 的实际 serializer 映射，不凭语言习惯猜测。

## Change Routing

- **Additive**：新增可选字段通常可兼容，但仍检查严格客户端、签名校验和缓存 key。
- **Breaking**：重命名/删除字段、收紧 nullable、改变类型/枚举/状态码或语义时，先确认版本化、双写/双读或迁移窗口。
- **Bug fix**：先用契约测试复现线上 payload；在 producer 或 consumer 的单一正确边界修复，不在多层散落兼容补丁。
- **Unknown protocol**：代码、旧协议与测试无法确认时标记 unknown，增加原始 payload/字节调试证据，不把猜测写入文档。

## Workflow

1. 建立 `producer -> wire format -> consumer` 字段矩阵并标出不一致。
2. 选择唯一契约来源；已有 OpenAPI/schema 时更新生成链路，不手改会被覆盖的生成文件。
3. 设计兼容策略与错误语义，再同步 endpoint、DTO/types、service 映射、测试和示例。
4. 运行序列化/契约测试，并用代表性 payload 验证双向映射；可行时启动两端验证真实请求。
5. 明确行为变化、迁移要求和仍未验证的消费者。

## Guardrails

- 公共破坏性变更、未知字段语义或会影响外部消费者的选择必须先确认。
- 不依赖大小写不敏感、宽松 JSON coercion 或默认 enum 转换来掩盖契约错误。
- 不暴露实体模型作为默认公共 DTO；仅在现有项目明确采用该模式且风险可接受时沿用。
