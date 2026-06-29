# Task 5 学习记录：选择性加入暂存区

## 任务目标

- 使用明确路径选择要进入下一次提交的文件。
- 区分工作目录、暂存区和提交历史。
- 在提交前检查暂存文件与变化摘要。

## 实际操作

选择性暂存了：

```text
.gitignore
TASK_01_ENVIRONMENT_AND_CLI.md
TASK_02_GIT_INIT.md
TASK_03_REPOSITORY_FILE_CLASSIFICATION.md
TASK_04_GITIGNORE.md
```

没有使用 `git add .`，医学数据没有进入暂存区。

## 核心理解

### `git add` 不会移动文件

文件本体仍位于工作目录。`git add` 把所选文件当时的内容快照写入暂存区：

```text
工作目录 --git add--> 暂存区 --git commit--> 提交历史
```

- `Changes to be committed`：暂存区中将进入下一次提交的变化。
- `Untracked files`：存在于工作目录，但尚未进入 Git 索引的文件。

### 暂存区不一定是工作目录的最新版本

文件执行 `git add` 后如果继续编辑：

- 暂存区保留执行 `add` 时的旧快照。
- 工作目录保存编辑后的新内容。
- `git status` 可以同时显示待提交变化和未暂存变化。

再次对该文件执行 `git add`，会用工作目录中的当前内容更新暂存区快照。

### 暂存区没有自己的版本历史

重新执行 `git add` 会覆盖该文件当前的索引快照。Git 不会把每一个旧暂存版本保存为历史；正式提交才形成可引用的版本历史。

## 检查暂存内容

查看暂存变化摘要：

```powershell
git diff --cached --stat
```

- `diff`：比较差异。
- `--cached`：比较暂存区与最近提交。
- `--stat`：只显示文件及行数变化摘要。

因为当前尚无提交，最近提交一侧相当于空基线。最终摘要为：

```text
5 files changed, 521 insertions(+)
```

查看指定文件的暂存差异：

```powershell
git diff --cached -- .gitignore
```

其中 `--` 将命令选项与文件路径分开。

输出中的：

```text
--- /dev/null
+++ b/.gitignore
@@ -0,0 +1,2 @@
```

表示旧基线中没有这个文件，暂存区中新建了一个包含两行内容的文件。以 `+` 开头的内容是新增行。

## 换行符警告

暂存 Markdown 文件时出现：

```text
LF will be replaced by CRLF
```

- LF：Linux 常用换行格式。
- CRLF：Windows 常用换行格式。
- `warning` 表示操作通常仍已完成。
- `fatal` 表示当前操作无法继续。

本 Task 只识别警告，暂不调整换行策略。

## 独立复现

在 `.gitignore` 已暂存后，再编辑工作目录版本并添加说明性注释。独立完成：

- 识别同一文件同时存在暂存版本与未暂存修改。
- 只重新暂存 `.gitignore`。
- 验证未暂存修改消失。
- 使用暂存差异确认注释已进入索引。
- 判断下一次提交将记录注释后的版本。

## 能力等级

- 知道（Know）：达到
- 理解（Understand）：达到
- 会实现（Implement）：达到
- 能独立完成（Independent）：达到

Task 5：已完成，进入 Review Pool（复习池）。

## Debug 能力评价

- 能通过 `git status` 判断文件处于未跟踪、已暂存或未暂存修改状态。
- 能区分警告与致命错误。
- 将 `--cached` 错写为无效参数后，能依据报错自行改正。
- 能使用差异输出证明具体内容已经进入暂存区。
- 曾在要求“先 Review、不要执行”时提前执行命令，流程纪律仍需强化。

Debug 当前评价：基础向进阶过渡。

## 当前薄弱点

- 容易混淆工作目录的最新内容与暂存区快照。
- 命令和参数拼写仍不稳定。
- 需要严格执行“计划、Review、执行、验证”的操作顺序。
- 对换行符和 Git 差异输出只具备初步认识。
