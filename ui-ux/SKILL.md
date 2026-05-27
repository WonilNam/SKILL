---
name: ui-ux
description: 高级 UI/UX、前端交互和视觉质量技能。用于新页面、新组件、复杂交互、样式重构、设计系统落地、响应式布局、动效、Canvas/WebGL/Three.js、可用性问题、dashboard/工具界面和高级视觉效果；当任务涉及界面结构、状态流转、交互反馈、视觉规范或前端质量验收时使用。
---

# UI/UX Skill

目标：做出和项目一致、功能完整、视觉精致、状态稳定的界面。设计必须服务使用场景，不做空壳营销页。

## Design Routing

- **Existing UI change**：先找同类页面和组件，沿用组件库、tokens、间距、交互模式。
- **New component/page**：先定义信息架构、组件树、状态流和验收状态。
- **Dashboard/tool**：优先密度、扫描、表格/筛选/操作效率、稳定布局。
- **Marketing/brand page**：首屏必须清楚传达对象/品牌/产品，视觉资产要真实相关。
- **Advanced visual**：粒子、光效、glass、3D、WebGL 必须不遮挡内容、不拖慢核心交互。

## Workflow

1. **Context Scan**：读取现有页面、组件、样式、UI 库、图标库、设计 tokens、路由和状态管理。
2. **User Task**：明确用户要完成的动作，不以视觉效果替代功能。
3. **Component Tree**：拆容器、展示、复用、业务组件；避免所有逻辑堆在一个大组件。
4. **State Model**：local、global/store、URL、server、form、derived、loading/error/empty。
5. **Interaction Map**：点击、输入、提交、取消、重试、禁用、权限、成功、失败、移动端。
6. **Visual System**：布局、层级、间距、颜色、字体、图标、动效、响应式约束。
7. **Implementation**：沿用现有技术栈和组件库；只在有明确收益时引入新依赖。
8. **QA**：运行页面，检查溢出、重叠、空白、可读性、焦点、移动端和关键交互。

## Visual Quality Rules

- 工具型界面：克制、清晰、可重复操作；不要用大 hero 和装饰卡片稀释功能。
- 高级视觉：可用 Canvas/WebGL/Three.js，但必须有稳定尺寸、性能边界和降级效果。
- 文字：不能溢出按钮/卡片/表格；移动端要换行或调整布局，不用 viewport 字体缩放。
- 图标：优先使用项目已有图标库；常见操作用图标按钮加 tooltip。
- 卡片：只用于重复项、modal 或真正需要框定的工具；不要卡片套卡片。
- 响应式：固定格式元素要有 `aspect-ratio`、min/max、grid track 或容器约束，避免状态变化导致跳动。
- 可访问性：交互元素要有可见状态、禁用态、焦点态和明确反馈。

## Confirmation Gates

需要确认：

- 引入新 UI/动画/3D 库或大型资源。
- 视觉方向明显偏离现有产品。
- 交互方案影响业务流程或数据语义。
- 需要真实品牌素材、设计稿或用户画像，但当前缺失。

不需要确认：

- 沿用现有设计系统的小改动。
- 修复布局破损、溢出、状态缺失、响应式问题。
- 补齐 loading/empty/error/disabled 等标准状态。

## Output Contract

```text
UI Intent:
Existing Patterns:
- <path>:<line> — <pattern to follow>
Component Tree:
State Model:
Interactions:
Visual Rules:
QA:
```

## Guardrails

- 不做没有真实功能的 landing 壳。
- 不用新风格覆盖项目已有风格，除非用户要求 redesign。
- 不让动效、辉光或 3D 抢走可读性和操作性。
- 实现后如果页面需要浏览器运行，实际打开并检查关键 viewport。
