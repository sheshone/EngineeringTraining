# Task 9 学习记录：创建第一个最小 Python 环境检查脚本

## 任务目标

- 创建项目中的第一个最小 Python 脚本。
- 检查当前 Python 解释器路径。
- 检查 PyTorch 是否能导入并输出版本。
- 检查医学数据目录是否存在。
- 理解“脚本路径”和“当前工作目录”的区别。

本 Task 不涉及 Dataset、DataLoader、模型、训练循环或 CUDA 检查。

## 文件位置

脚本应放在：

```text
src/check_environment.py
```

不是项目根目录下的：

```text
check_environment.py
```

## 当前脚本内容

```python
import sys
import torch
import pathlib

print("Python executable:", sys.executable)
print("Pytorch version:", torch.__version__)
print("Data directory exists:", pathlib.Path("MedMNIST_Blood_Path_Organ_128").exists())
```

当前脚本保持最小形式，没有函数、类、参数解析和 CUDA 检查。

## 运行方式

从项目根目录运行：

```powershell
python .\src\check_environment.py
```

成功输出：

```text
Python executable: D:\anaconda\envs\pytorch\python.exe
Pytorch version: 2.8.0+cpu
Data directory exists: True
```

## 遇到的问题

### 1. 拼写错误导致语法错误

曾写成：

```python
improt torch
```

这是 Python 语法错误，因为导入关键字应为：

```python
import
```

这类错误会在 Python 解析代码阶段失败，还没进入 PyTorch 导入阶段。

### 2. 使用 `pathlib.Path` 前需要导入

如果写：

```python
pathlib.Path(...)
```

需要先写：

```python
import pathlib
```

另一种写法是：

```python
from pathlib import Path
```

然后使用：

```python
Path(...)
```

本 Task 当前采用 `import pathlib`。

### 3. 脚本路径错误

曾运行：

```powershell
python check_environment.py
```

失败原因是当前工作目录 `F:\medMNIST` 下没有这个文件。

正确文件在：

```text
F:\medMNIST\src\check_environment.py
```

因此应运行：

```powershell
python .\src\check_environment.py
```

## 核心理解

### `sys.executable`

`sys.executable` 输出当前正在运行脚本的 Python 解释器路径。

它能帮助确认当前是否使用了正确的 conda 环境。例如本次输出：

```text
D:\anaconda\envs\pytorch\python.exe
```

说明脚本运行在 `pytorch` 环境中。

### `torch.__version__`

`torch.__version__` 输出当前安装的 PyTorch 版本。

本次输出：

```text
2.8.0+cpu
```

说明当前 PyTorch 是 CPU 构建。

它不能证明 CUDA 可用。CUDA 是否可用需要单独检查，例如：

```python
torch.cuda.is_available()
```

但本 Task 暂时不加入 CUDA 检查。

### 相对路径相对于当前工作目录

代码：

```python
pathlib.Path("MedMNIST_Blood_Path_Organ_128").exists()
```

不是天然相对于脚本所在目录，也不是天然相对于项目根目录。

它相对于“当前工作目录”计算。

本次从项目根目录：

```text
F:\medMNIST
```

运行脚本，所以检查的是：

```text
F:\medMNIST\MedMNIST_Blood_Path_Organ_128
```

因此返回 `True`。

如果先进入：

```powershell
cd .\src
```

再运行脚本，那么当前工作目录变成：

```text
F:\medMNIST\src
```

这时相对路径会检查：

```text
F:\medMNIST\src\MedMNIST_Blood_Path_Organ_128
```

通常会返回 `False`。

## Task Assessment 状态

### 实现部分

已通过：

1. 文件位于 `src/check_environment.py`。
2. 能从项目根目录运行。
3. 能输出 Python 解释器路径。
4. 能输出 PyTorch 版本。
5. 能检查数据目录是否存在。
6. 不报错。

### 概念部分

第一次回答中误以为相对路径天然相对于项目根目录。

修正后能正确说明：

- 相对路径相对于当前工作目录。
- 从 `src/` 中运行脚本时，数据目录检查可能变成 `False`。

### Independent

已通过。

闭卷回答中能够独立说明：

- 脚本位于 `src/`，完整路径为 `.\src\check_environment.py`。
- 使用了 `sys`、`torch` 和 `pathlib`。
- 三项输出分别检查 Python 解释器、PyTorch 版本和数据目录。
- 应从项目根目录运行 `python .\src\check_environment.py`。
- 相对路径的解析结果取决于当前工作目录。

回答 `.\src` 时路径不完整，经追问后能够补充完整命令，不影响本次通过。

Task 9 目前状态：

- 知道（Know）：达到
- 理解（Understand）：达到
- 会实现（Implement）：达到
- 能独立完成（Independent）：达到

Task 9 已完成，进入 Review Pool。

## Debug 能力评价

- 能识别 `improt` 属于语法错误。
- 能根据报错理解 `python check_environment.py` 找错了文件路径。
- 能修正路径并成功运行脚本。
- 对“当前工作目录”和“脚本所在目录”的区别一开始不稳，修正后理解。

Debug 当前评价：能够识别语法、导入和脚本路径问题，并解释相对路径的判断依据；本 Task 达到通过标准。

## 当前薄弱点

- Python import 拼写。
- 模块导入方式：`import pathlib` 与 `from pathlib import Path`。
- 当前工作目录与脚本路径的区别。
- 从不同目录运行脚本时，相对路径结果会变化。
