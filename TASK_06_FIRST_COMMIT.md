# Task 6 学习记录：创建第一次 Git 提交

## 任务目标

- 在提交前检查暂存区。
- 创建有意义的本地提交。
- 理解提交对象、哈希、HEAD、分支和 message。
- 区分本地 commit 与远程 push。

## 主项目第一次提交

第一次提交最终修正为：

```text
7379829 docs: 初始化学习记录与复习池
```

提交包含：

- `.gitignore`
- `REVIEW_POOL.md`
- Task 1～5 学习记录

共 7 个文件、704 行新增。医学数据没有进入提交。

## 核心理解

### commit 保存什么

`git commit` 把暂存区的整体快照写入本地提交历史，不会自动保存工作目录中尚未暂存的修改，也不会自动上传到远程。

### 提交对象与哈希

提交对象包含文件树、父提交、作者、提交者、时间和 message 等信息。任一内容改变，提交对象的哈希通常都会改变。

```text
7379829 (HEAD -> main)
```

- `7379829`：提交哈希缩写。
- `main`：当前分支。
- `HEAD -> main`：HEAD 当前指向 `main`，而 `main` 指向该提交。

### amend 的机制

`git commit --amend` 不会原地修改旧对象，而是创建新提交对象，再移动当前分支指针。

普通 `git log` 从当前分支出发沿父提交链查看可达历史。被替换的旧提交不在新提交的父链中，因此不再显示；reflog 记录指针曾经的位置，短期内仍可能找到旧对象。

### commit 与 push

- `commit`：在本地 `.git` 中创建提交。
- `push`：把本地提交发送到已配置的远程仓库。
- `git remote -v` 无输出表示当前没有配置远程地址。

### message 与 `docs:`

`docs:` 不是 Git 强制语法，而是一种便于阅读和分类的 Conventional Commits 风格。本次主要增加学习文档，因此使用 `docs:`。

提交消息编辑器中以 `#` 开头的行是说明注释，不会成为正式 message。只留下这些行会导致空消息并中止提交。

## 遇到的问题

### `git add.` 与 `git add .`

- `git add.`：`add.` 被解析为不存在的子命令。
- `git add .`：`.` 是当前目录路径，会选择其下所有未被忽略的变化。

本 Task 要求明确选择文件，但第一次操作跳过 Review 并使用了 `git add .`。虽然数据被 `.gitignore` 排除，没有造成错误提交，但流程纪律不合格。

### 暂存检查命令拼写

练习中曾把：

```text
git diff --cached --stat
```

错误写成 `-cache`、`-stat`，甚至去掉 `git` 后调用了 PowerShell 的 `diff` 别名。第一次练习因此未通过 Assessment，因为检查失败后仍继续提交。

## Task Assessment

在独立仓库 `F:\test` 中重新进行完整 Assessment：

1. 修改已跟踪的 `test.txt`。
2. 使用 `git status` 识别未暂存修改。
3. 只暂存 `test.txt`。
4. 提交前成功运行暂存差异检查，确认 `1 insertion(+)`。
5. 创建本地提交。
6. 验证工作区干净。
7. 使用 `git log --oneline -1` 验证：

```text
987aa9e (HEAD -> main) docs:added a meaningful line to test.txt
```

8. 正确解释该操作没有涉及远程仓库。

第二次 Assessment 全程按顺序完成，没有跳过失败的验证步骤。

## 能力等级

- 知道（Know）：达到
- 理解（Understand）：达到
- 会实现（Implement）：达到
- 能独立完成（Independent）：达到

Task 6：已完成，进入 Review Pool（复习池）。

## Debug 能力评价

- 能识别未暂存、已暂存和已提交状态。
- 能利用 `status`、暂存 diff、log 和 show 进行验证。
- 能理解空 message、无效选项和命令归属错误。
- 第一次遇到检查错误时选择绕过，第二次 Assessment 已能停止、修正并完成验证。

Debug 当前评价：基础向进阶过渡。命令拼写和执行纪律仍需持续复习。

## 当前薄弱点

- 长选项的双短横线和精确名称。
- 从错误输出中提取正确用法。
- commit、amend、log 与 reflog 的对象关系。
- 执行前等待 Review，以及失败后不绕过验证。
