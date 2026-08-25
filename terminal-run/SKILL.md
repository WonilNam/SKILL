---
name: terminal-run
description: 在本地终端中运行构建、测试、类型检查、lint、脚本、开发服务器或只读诊断，并用真实输出验证工程结论。当任务需要复现错误、确认修复、收集日志或判断环境问题时使用；不因仅展示一条命令或讨论理论结果而触发执行。
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

“test”“dev”“start”等脚本名称不代表无副作用。首次运行前读取对应 script/config；如果会连接非隔离数据库、执行迁移/seed、调用真实外部服务、发送消息、发布或清理数据，按实际副作用进入授权门禁。

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

- Dev server：启动后确认 URL、端口、关键日志；记录进程并在验证结束后关闭，除非用户要求持续运行。
- Watch mode：除非用户要求持续运行，否则避免用 watch 命令作为验证。
- Timeout：超时不是失败结论，要说明超时点和已看到的输出。

## Result Reporting

命令只是任务中的验证步骤时，最终只摘要命令、结果和关键错误；用户明确要求执行报告时使用完整结构：

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
- 严禁编造或凭空想象终端命令的输出。如果无法运行或工具未安装，必须在结果中明确归类为 env-error，并展示真实报错。
- 区分“命令成功”和“需求已验证”：退出码为 0 也可能没有覆盖目标行为，必须说明验证范围。
