# Task 8 学习记录：创建最小项目结构

## 任务目标

- 建立一个最小但清晰的 AI 项目骨架。
- 理解 `src/`、`notebooks/`、`outputs/` 的职责边界。
- 理解 Git 为什么不追踪空目录。
- 学会用 `.gitkeep` 保留需要追踪的空目录。
- 继续训练 PowerShell 的基础文件操作命令。

## 本 Task 创建的结构

```text
F:\medMNIST
├── src/
│   └── .gitkeep
├── notebooks/
│   └── .gitkeep
└── outputs/
```

`.gitignore` 新增：

```text
/outputs/
```

## 目录职责

### `src/`

放正式源码。以后项目中的核心 Python 代码会放在这里，例如：

- 数据读取代码
- Dataset 定义
- 模型定义
- 训练脚本
- 推理脚本

原则：`src/` 放可以重复运行、可以维护、可以交给别人阅读的正式代码。

### `notebooks/`

放探索性 Notebook，例如：

- 查看医学图像样子
- 检查 label 分布
- 做小规模可视化
- 验证临时想法

Notebook 可以用于探索，但不作为长期训练流程的核心入口。

### `outputs/`

放运行产生的输出，例如：

- 日志
- checkpoint
- 可视化图片
- 混淆矩阵
- 推理结果

这类内容通常可重新生成、体积可能较大、变化频繁，所以默认不进入 Git。

## 核心理解

### Git 不追踪空目录

Git 追踪的是文件快照，不直接追踪空目录。

如果一个目录里没有任何文件，Git 没有可保存的文件对象，因此 `git status` 不会把这个空目录列为可追踪内容。

### `.gitkeep` 的作用

`.gitkeep` 不是 Git 官方规定的特殊文件。

它只是社区习惯使用的普通空文件。因为 Git 可以追踪文件，所以在空目录里放一个 `.gitkeep`，就能通过追踪这个文件来间接保留目录结构。

本 Task 中：

```text
src/.gitkeep
notebooks/.gitkeep
```

会被 Git 追踪。

但 `outputs/` 不放 `.gitkeep`，因为它是输出目录，本来就不准备追踪。

### `modified` 与 `untracked`

本 Task 完成但尚未 `git add` 时，`git status` 应该显示：

```text
modified:   .gitignore
Untracked files:
        notebooks/
        src/
```

含义：

- `modified`：已被 Git 跟踪过的文件，现在工作目录版本发生了变化。
- `untracked`：还没有进入 Git 跟踪体系的新文件或目录。

虽然 `git status` 显示的是 `src/` 和 `notebooks/`，但真正会被追踪的是：

```text
src/.gitkeep
notebooks/.gitkeep
```

## PowerShell 命令模板

创建目录：

```powershell
New-Item -ItemType Directory -Path .\src
```

创建文件：

```powershell
New-Item -ItemType File -Path .\src\.gitkeep
```

查看目录并显示隐藏内容：

```powershell
Get-ChildItem -Force .\src
```

推荐在 Windows PowerShell 中统一使用反斜杠路径：

```text
.\scripts
.\scripts\.gitkeep
F:\medMNIST\scripts
```

## 遇到的问题

### 混淆 `.gitignore` 目标

最初计划中曾想把 `notebooks` 写进 `.gitignore`。

修正后理解为：

- `src/`：应该追踪。
- `notebooks/`：本阶段保留目录结构，追踪 `.gitkeep`。
- `outputs/`：运行输出，应忽略。

### 误以为 `.gitkeep` 是 Git 官方特殊文件

修正后理解为：`.gitkeep` 只是普通空文件，用作占位。

### PowerShell 参数格式不稳定

曾写成：

```powershell
New-Item -ItemType File Path F:\medMNIST\notebooks\.gitkeep
New-Item -ItemType Directory - Path .\src
```

问题分别是：

- `Path` 前缺少 `-`。
- `-Path` 被错误拆成 `- Path`。

正确写法：

```powershell
New-Item -ItemType File -Path .\notebooks\.gitkeep
New-Item -ItemType Directory -Path .\src
```

### 混淆列目录命令

曾把列目录命令写成：

```powershell
Item-List -Path ./scripts -Force
```

修正为：

```powershell
Get-ChildItem -Force .\scripts
```

## Task Assessment

### 实现检查

已完成：

1. 创建 `src/`。
2. 创建 `notebooks/`。
3. 创建 `outputs/`。
4. 创建 `src/.gitkeep`。
5. 创建 `notebooks/.gitkeep`。
6. 修改 `.gitignore`，加入 `/outputs/`。
7. 验证 `outputs/` 不出现在 `git status` 的 untracked 列表中。

### 概念 Assessment

最初回答中：

- 误以为 Git 不追踪“根目录”。
- 误以为 `.gitkeep` 是 Git 官方特殊文件。
- 漏掉 `.gitignore` 会出现在 `modified` 状态中。

修正后能正确说明：

- Git 追踪文件快照，不追踪空目录。
- `.gitkeep` 是普通占位文件，不是官方特殊机制。
- `git add src notebooks .gitignore` 真正暂存的是 `src/.gitkeep`、`notebooks/.gitkeep` 和 `.gitignore`。
- 当前未暂存状态下，`.gitignore` 是 `modified`，`src/` 和 `notebooks/` 是 `untracked`，`outputs/` 不应出现。

### 独立复现 Assessment

第一次独立复现未通过，原因是 PowerShell 命令模板没有记住。

随后进行了最小命令模板训练：

```powershell
New-Item -ItemType Directory -Path .\src
New-Item -ItemType Directory -Path .\notebooks
New-Item -ItemType Directory -Path .\outputs
New-Item -ItemType File -Path .\src\.gitkeep
New-Item -ItemType File -Path .\notebooks\.gitkeep
```

经过纠错后，能独立写出这 5 条命令，并能解释最终 Git 状态。

## 能力等级

- 知道（Know）：达到
- 理解（Understand）：达到
- 会实现（Implement）：达到
- 能独立完成（Independent）：达到，但仍偏脆弱

Task 8：已完成，进入 Review Pool（复习池）。

## Debug 能力评价

- 能根据 `git status` 判断 `.gitignore`、`src/`、`notebooks/`、`outputs/` 的状态是否符合预期。
- 能通过纠错理解 PowerShell 参数必须写成 `-Path`，不能写成 `Path` 或 `- Path`。
- 能区分 Git 命令与 PowerShell 命令。
- 仍需继续训练相对路径、参数拼写和命令名称。

Debug 当前评价：基础可用，但命令模板仍不够稳定，需要在后续 Task 中持续短频复现。

## 当前薄弱点

- PowerShell 命令模板记忆。
- 相对路径 `.\目录` 的使用。
- 参数名必须整体书写，例如 `-Path`。
- `modified` 与 `untracked` 的状态判断。
- 空目录、占位文件、忽略规则三者之间的关系。
