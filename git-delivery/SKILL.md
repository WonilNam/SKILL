---
name: git-delivery
description: 准备、审查或执行 Git 交付流程，包括工作区检查、聚焦 diff、分支、commit、push、PR 或 release 前验证。当用户明确要求提交、推送、建分支、准备 PR/发布或 Git 交付审查时使用；普通代码 review、仅实现代码或查看 git status 不代表授权 commit/push。
---

# Git Delivery

目标：只交付当前任务的已验证改动，保留用户工作区和历史，不扩大外部写入权限。

## Authorization Routing

- **Prepare/review**：允许只读检查 status、diff、branch、remote、log 和验证结果；不给远端写入。
- **Commit**：仅用户明确要求 commit/提交时执行；提交前检查 staged diff，不自动混入无关文件。
- **Push/PR/release**：分别需要用户明确要求相应外部动作；push 失败不 force push，release 不从“准备发布”推断授权。
- **History rewrite/destructive cleanup**：reset、rebase、force push、clean、restore/checkout 覆盖改动需要明确且具体授权，并先确认精确目标。

## Workflow

1. 读取 `git status --short`、当前分支、仓库根和相关 diff，区分任务改动、用户已有改动、生成物与临时文件。
2. 根据变更风险运行相关测试、构建、类型检查和文档验证；失败时停止交付并报告第一条关键错误。
3. 检查新增文件、删除、配置、schema/API/协议和文档是否成套；确认没有凭据、日志、缓存或构建产物。
4. 仅暂存当前任务文件，复查 staged diff；提交信息使用“动词 + 具体对象 + 目的”。
5. push 前确认 branch 与 remote；新分支默认 `codex/` 前缀。PR 摘要说明行为变化、测试和已知风险。

## Completion Report

报告实际执行的动作、commit hash/分支（如有）、验证结果和未交付文件。没有明确 commit/push 授权时，只给建议命令或提交信息，不执行。

## Guardrails

- 不使用 `git reset --hard` 或 `git checkout -- .`。
- 不覆盖、恢复或删除无法归因于当前任务的未提交改动。
- 不用 `git add .` 掩盖范围判断；按明确文件暂存并复查。
- 不因用户说“完成”“修好”而推断 commit、push、PR 或 release 权限。
