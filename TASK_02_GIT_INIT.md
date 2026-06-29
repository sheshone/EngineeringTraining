# Task 2 学习记录：初始化 Git 仓库

## 任务目标

- 把普通项目目录初始化为 Git 仓库。
- 认识 `.git`、仓库根目录和未跟踪文件。
- 理解工作目录、暂存区和提交历史之间的关系。

## 执行结果

在 `F:\medMNIST` 执行：

```powershell
git init
```

Git 成功创建了空仓库：

```text
Initialized empty Git repository in F:/medMNIST/.git/
```

`Get-ChildItem -Force` 显示新出现了隐藏目录 `.git`。

仓库根目录检查结果：

```text
F:/medMNIST
```

## 遇到的问题与理解

### 1. exFAT 与 dubious ownership

`git status` 最初报错：

```text
fatal: detected dubious ownership in repository at 'F:/medMNIST'
'F:/medMNIST' is on a file system that does not record ownership
```

检查发现 `F:` 使用 exFAT 文件系统。exFAT 没有提供 Git 用于验证仓库所有者的完整所有权信息，因此 Git 无法确认仓库是否属于当前用户，并触发安全保护。

把具体目录加入信任名单：

```powershell
git config --global --add safe.directory F:/medMNIST
```

这里：

- `--global` 表示配置保存在当前用户的 Git 全局配置中。
- `safe.directory F:/medMNIST` 只信任指定目录，不代表信任所有目录。

### 2. 命令参数拼写

错误写法：

```text
git rev-parse -show-toplevel
```

正确写法：

```text
git rev-parse --show-toplevel
```

长选项通常使用两个短横线，但仍应以具体命令的帮助信息为准。

### 3. 什么是 untracked files

Git 报告以下内容尚未跟踪：

```text
MedMNIST_Blood_Path_Organ_128/
TASK_01_ENVIRONMENT_AND_CLI.md
```

`untracked` 表示文件或其中的文件真实存在于工作目录，但尚未被加入 Git 的索引。它不表示文件丢失，也不表示文件已经提交。

### 4. Git 的三个基础阶段

```text
工作目录 --git add--> 暂存区 --git commit--> 提交历史
```

- 工作目录：当前实际看到和编辑的文件。
- `git add`：把所选文件当前内容的快照写入暂存区。
- 暂存区：准备进入下一次提交的快照集合，也称 staging area 或 index。
- `git commit`：把暂存区的整体快照记录到版本历史。

文件并不会在硬盘目录之间被物理移动。

### 5. Git 跟踪文件而不是目录

Git 主要记录文件内容及路径，不直接记录空目录。完全没有文件的目录通常没有可供 Git 保存的内容。

`.git` 只位于仓库根目录，用于保存整个仓库的版本控制元数据，不需要每个子目录各有一个 `.git`。

## 为什么暂时不执行 `git add .`

项目中包含医学图像数据目录。数据集通常体积较大，不适合未经筛选直接写入普通 Git 历史。在建立忽略规则之前，不应把整个目录一次性加入暂存区。

## 面试验收结论

- 能确认 `git init` 已创建仓库。
- 能识别仓库根目录与 `.git`。
- 能解释 `untracked` 不代表文件丢失。
- 初步理解全局配置作用域与具体配置值的区别。
- 能区分 `git add` 和 `git commit`。
- 理解 Git 不直接跟踪空目录。

## 能力等级

- 知道（Know）：达到
- 理解（Understand）：达到
- 会实现（Implement）：达到
- 能独立完成（Independent）：达到

## 独立复现

第一次复现误在 `F:\medMNIST\gitexe` 中创建嵌套仓库，之后又误在 `F:\` 根目录初始化仓库。通过检查仓库根目录和 `git status` 的管理范围，识别并安全删除了 `F:\.git`，同时精确移除了误加的 `safe.directory=F:/`，没有影响磁盘中的实际文件。

最终在独立目录 `F:\test` 中完成复现：

- 初始化空仓库。
- 找到隐藏的 `.git`。
- 根据 exFAT 安全检查报错，仅将 `F:/test` 加入信任名单。
- 独立修正多处命令和参数拼写错误。
- 查询仓库根目录。
- 创建 `test.txt` 并正确识别为未跟踪文件。
- 确认原嵌套仓库的 `.git` 已删除。

Task 2：最终通过。

## Debug 能力评价

- 看懂报错：能区分“命令不存在”“参数不存在”和 Git 所有权安全检查
- 定位问题：能够利用报错信息定位拼写与安全配置问题
- 推测原因：能够联系 exFAT 和仓库信任范围，但目录作用域仍需继续强化
- 独立修复：能根据报错建议完成最小范围修复，并重试验证

Debug 当前评价：基础向进阶过渡。独立纠正拼写的能力明显提升，但执行 `git init`、删除和全局配置等高影响操作前，仍需养成先检查当前路径和影响范围的习惯。

## 当前薄弱点

- Git 配置、配置作用域和配置值的区别。
- 工作目录、暂存区和提交历史的精确术语。
- 容易把“记录文件快照”理解成“物理移动文件”。
- 命令长选项中短横线数量的精确性。
