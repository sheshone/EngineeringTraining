# Task 7 学习记录：小而完整的增量提交

## 任务目标

- 在已有提交之后，完成一次小范围增量提交。
- 形成固定流程：检查 → 暂存 → 再检查 → 提交 → 验证。
- 理解工作目录修改、暂存区快照和提交历史之间的关系。
- 训练检查命令失败后停止 Debug，而不是绕过检查继续提交。

## 本 Task 的核心流程

一次合格的增量提交，不是只看最后有没有 commit 成功，而是看提交前是否确认过暂存区内容。

最小流程是：

1. 修改文件后，用 `git status` 确认工作目录状态。
2. 用 `git add <file>` 只暂存目标文件。
3. 再用 `git status` 确认哪些内容进入暂存区。
4. 用 `git diff --cached --stat` 查看暂存区摘要。
5. 必要时用 `git diff --cached -- <file>` 查看具体差异。
6. 确认无误后再 `git commit -m "type: message"`。
7. 用 `git log --oneline -1` 和 `git status` 验证结果。

## 核心理解

### 工作目录修改不会自动进入提交

文件被修改以后，只是工作目录发生变化。暂存区不会自动更新，提交历史也不会自动更新。

如果一个文件先 `git add`，之后又继续编辑，那么暂存区里仍是上一次 `add` 时的快照。想让新修改进入下一次提交，需要再次 `git add`。

### `git diff --cached` 比较什么

`git diff --cached` 查看的是“暂存区相对于最近一次提交”的差异。

它回答的问题是：

> 如果我现在 commit，会把哪些变化写进下一次提交？

`--stat` 只看摘要；不加 `--stat` 可以查看具体补丁。

### `--` 是路径分隔符

在命令：

```text
git diff --cached -- test.txt
```

中，第二个 `--` 是分隔符。它表示后面开始是路径，不再是 Git 选项或提交名。

因此下面写法是错误的：

```text
git diff --cached --"test.txt"
```

原因是 `--` 和路径粘在一起后，不再是独立分隔符。

### `--oneline` 是长选项

`git log --oneline -1` 中：

- `--oneline`：长选项，把每个提交压缩为一行显示。
- `-1`：短选项，只显示最近 1 条提交。

不能把 `--oneline` 写成 `-oneline`。单短横线和双短横线不是可以随意替换的装饰。

### diff 中“删掉又加回一样的行”

当文件末尾原本没有换行符时，新增下一行会改变上一行的行尾状态。

Git 按“行”比较，所以可能显示：

- 删除旧的“无换行结尾”的行。
- 新增同样文本但带换行的行。
- 再新增真正的新行。

这不是内容真的重复删除，而是行尾换行状态发生了变化。

## 遇到的问题

### 第一次 Assessment 未通过

在 `F:\test` 中，用户完成了修改、暂存、提交和验证，但出现了两个问题：

1. `git diff --cached --"test.txt"` 失败后，没有先停下来解释错误原因，而是绕过后继续。
2. commit message 写成 `test:add third text`，冒号后没有空格。

这说明功能结果虽然成功，但独立工程流程还没有通过。

### 补充 Debug 训练

针对“检查失败后是否停下来”，进行了 4 个问题训练：

1. 为什么 `git diff --cached --"test.txt"` 失败？
2. 为什么 `git log -oneline -1` 失败？
3. `--cached` 和 `-oneline` 的写法差别是什么？
4. 检查命令失败后，commit 前应该做什么？

最终形成的 Debug 动作链是：

1. 不继续 commit。
2. 读报错，找原因。
3. 检查状态，必要时改正命令后重新验证。

## Task Assessment

最终独立 Assessment 在 `F:\test` 中完成：

1. 修改 `test.txt`，新增一行。
2. `git status` 显示 `test.txt` 已修改但未暂存。
3. `git add test.txt` 只暂存目标文件。
4. `git status` 显示 `test.txt` 已进入暂存区。
5. `git diff --cached --stat` 成功显示摘要：

```text
test.txt | 3 ++-
1 file changed, 2 insertions(+), 1 deletion(-)
```

6. `git diff --cached -- test.txt` 成功查看具体差异。
7. 使用合格格式提交：

```text
test: fourth add
```

8. `git log --oneline -1` 验证最新提交：

```text
08de201 (HEAD -> main) test: fourth add
```

9. `git status` 验证工作区干净。
10. 正确说明 `08de201` 是上一个提交 `54d49ed` 的子提交。

## HEAD 与 main 的理解

- `main` 是分支名，可以理解为当前历史线的指针。
- `HEAD` 表示当前所在位置。
- `HEAD -> main` 表示当前站在 `main` 分支上，而 `main` 指向当前最新提交。

## 能力等级

- 知道（Know）：达到
- 理解（Understand）：达到
- 会实现（Implement）：达到
- 能独立完成（Independent）：达到，但刚过线

Task 7：已完成，进入 Review Pool（复习池）。

## Debug 能力评价

- 能看懂 `git status` 的未暂存、已暂存、clean 状态。
- 能使用 `git diff --cached --stat` 和具体 diff 检查暂存内容。
- 能识别 `--oneline`、`--cached`、`-- <path>` 这类参数写法。
- 最初遇到检查命令失败时仍有绕过倾向；补考后能按要求完成完整流程。

Debug 当前评价：基础可用，但流程纪律仍需重点复习。尤其要训练“检查失败后不继续提交”。

## 当前薄弱点

- 长选项 `--xxx` 与短选项 `-x` 的区别。
- `--` 分隔符与路径之间必须有空格。
- commit message 的 `type: message` 格式。
- 暂存摘要异常时，要继续看具体 diff。
- 检查失败后停止，而不是绕过失败命令继续执行。
