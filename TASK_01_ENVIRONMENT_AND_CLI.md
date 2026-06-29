# Task 1 学习记录：开发环境与命令行

## 任务目标

- 确认当前工作目录。
- 识别正在使用的 Python 版本和解释器路径。
- 检查 PyTorch 版本与 CUDA 可用性。
- 检查 Git 环境及当前目录是否为 Git 仓库。
- 建立 PowerShell 与 Linux 基础命令的对应关系。

## 实际环境

- 工作目录：`F:\medMNIST`
- Conda 环境：`pytorch`
- Python：`3.9.23`
- Python 解释器：`D:\anaconda\envs\pytorch\python.exe`
- PyTorch：`2.8.0+cpu`
- CUDA 可用：`False`
- Git：`2.53.0.windows.1`
- `F:\medMNIST` 当前不是 Git 仓库

## 使用过的命令

```powershell
Get-Location
Get-ChildItem -Force
python --version
python -c "import sys; print(sys.executable)"
python -c "import torch; print(torch.__version__)"
python -c "import torch; print(torch.cuda.is_available())"
git --version
git status
```

## 遇到的问题与理解

### 1. Conda 命令拼写错误

错误写法：`conda activiate pytorch`

正确写法：`conda activate pytorch`

认识：命令和 API 名称必须精确匹配。

### 2. PyTorch API 拼写错误

错误写法：`torch.cuda.isavailable()`

正确写法：`torch.cuda.is_available()`

认识：Python 标识符中的下划线是名称的一部分，不能省略。

### 3. `sys` 是什么

`sys` 是 Python 标准库模块，用于访问解释器和运行环境信息。
`sys.executable` 返回当前实际运行的 Python 可执行文件路径，可用于确认 Conda 环境是否生效。

### 4. 为什么 CUDA 不可用

当前 PyTorch 版本带有 `+cpu`，说明安装的是 CPU 构建，因此不能通过它使用 CUDA。
CUDA 能否使用还涉及 NVIDIA GPU、驱动和 CUDA 版 PyTorch等条件。

### 5. `git status` 的报错是什么意思

报错：

```text
fatal: not a git repository (or any of the parent directories): .git
```

含义：当前目录及其父目录中没有找到 Git 仓库元数据。
这不能证明所有子目录都不是独立的 Git 仓库。

### 6. `.git` 是什么，来自哪里

`.git` 通常是 Git 仓库根目录中的隐藏目录，保存提交历史、文件对象、分支引用、配置和暂存区信息。

它通常由以下操作产生：

- `git init`
- `git clone`

仓库管理其根目录及后代目录，不会反向管理父目录。Git 从当前目录向父目录查找 `.git`，不会自动向所有子目录搜索。

### 7. PowerShell 与 Linux 命令对应

| 目的 | PowerShell | Linux |
|---|---|---|
| 查看当前目录 | `Get-Location` | `pwd` |
| 查看目录内容和隐藏项 | `Get-ChildItem -Force` | `ls -la` |

在 `ls -la` 中：

- `ls`：列出目录内容
- `-l`：显示详细信息
- `-a`：包括隐藏项

## 面试验收结论

- 能通过 `sys.executable` 验证当前 Python 来自哪个 Conda 环境。
- 能区分 Python 版本与解释器路径。
- 理解 PyTorch 有 CPU 构建和 CUDA 构建。
- 初步理解 Git 仓库具有明确的目录边界。
- 能识别 PowerShell 与 Linux 的基础目录查看命令。

Task 1：通过。

## 当前薄弱点

- 命令和 API 的精确拼写。
- Git 仓库的目录边界与查找方向。
- PowerShell 和 Linux 命令参数的记忆。
- CUDA 可用条件还需要后续反复巩固。
