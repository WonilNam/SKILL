---
name: terminal-run
description: 高级终端执行、复现和验证技能。用于运行构建、测试、类型检查、lint/format、脚本、开发服务器、诊断命令、环境探测和只读 Git 检查；当需要真实系统结果验证假设、复现错误、确认修复、收集日志或判断环境问题时使用。
---

# Terminal Run Skill

目标：用真实命令结果替代猜测。每次执行都要清楚目的、工作目录、风险等级、退出码和后续动作。

## Command Selection

先根据项目文件识别技术栈和包管理器：

- Node：看 `package.json`、lockfile 和 scripts；不要混用 npm/pnpm/yarn/bun。
- .NET：看 `.sln`、`*.csproj`、`global.json`、test project。
- Python：看 `pyproject.toml`、`requirements.txt`、`uv.lock`、`pytest.ini`。
- Go/Rust/Java：看 `go.mod`、`Cargo.toml`、`pom.xml`、`build.gradle`。

优先运行最小验证命令：

- 语法/类型：`npm run typecheck`、`tsc --noEmit`、`dotnet build`
- 单元测试：相关 test project、相关 test file、过滤后的 test case
- 全量验证：只有风险较高或提交前才扩大到全量测试/构建
- 复现问题：先运行最短复现路径，再改代码

## Execution Workflow

1. **Intent**：说明要验证什么假设。
2. **CWD**：确认工作目录，优先项目根目录。
3. **Risk Gate**：判断命令是 safe、write、destructive、external。
4. **Run**：设置合理 timeout；长命令需要观察输出。
5. **Classify**：success、build error、test failure、runtime error、env error、permission error、timeout。
6. **Act**：根据输出修复、缩小范围、扩大验证或说明无法继续。

## Safety Policy

默认允许：

- 构建、测试、类型检查、lint/format、只读查询、项目内 dev server。
- 只读 Git：`git status`、`git diff`、`git log`、`git show`、`git branch --show-current`。

需要用户明确要求或授权：

- 删除/清理：`rm -rf`、`Remove-Item -Recurse -Force`、`del /s`、`rmdir /s`、`git clean`。
- Git 历史/工作区破坏性操作：`git reset`、`git checkout --`、`git restore`、`git rebase`、`git push --force`。
- 远端或发布：commit、push、tag、release、publish。
- 系统级修改：`sudo`、注册表、系统目录、服务安装、全局 PATH 修改。
- 下载后执行：curl/wget/iwr 管道到 shell、未知安装脚本。
- 数据库破坏性命令：drop、truncate、生产迁移、清空数据。

Windows 文件操作规则：

- 删除/移动前解析绝对路径，并确认目标在预期工作区或用户明确指定目录内。
- 不跨 shell 拼接删除命令；优先用 PowerShell 原生命令和 `-LiteralPath`。

## Long-Running Commands

- Dev server：启动后确认 URL、端口、关键日志；不要在最终答复前留下不明状态。
- Watch mode：除非用户要求持续运行，否则避免用 watch 命令作为验证。
- Timeout：超时不是失败结论，要说明超时点和已看到的输出。

## Output Contract

```text
Command: <command>
CWD: <path>
Intent: <what this verifies>
Result: <success|build-error|test-failure|runtime-error|env-error|timeout>
Key Output:
- <important stdout/stderr lines>
Next:
- <fix, rerun, broaden validation, or explain blocker>
```

## Guardrails

- 不把未运行的命令写成已验证。
- 不隐藏 stderr 中的关键诊断。
- 不为“看起来应该可以”跳过可行验证。
- 命令失败时先读输出，不要盲目换方案。
