# Task 10: Inspect NPZ Dataset

## 目标

本 Task 的目标是认识 MedMNIST 的 `.npz` 数据文件结构。

本阶段不进入 Dataset、DataLoader 或训练流程，只做最小数据检查：确认文件存在、能被 NumPy 读取、内部 key 是否符合预期，以及图像和标签的基本 shape。

## 我检查了什么

- 使用 `pathlib.Path` 定位 `bloodmnist_128.npz`。
- 使用 `exists()` 和 `is_file()` 区分“路径存在”和“确实是文件”。
- 使用 `np.load(path)` 打开 `.npz` 容器。
- 使用 `data.files` 查看容器中的数组 key。
- 检查 `train_labels`、`val_images`、`val_labels` 的 shape 和 dtype。
- 检查验证集图像数量和标签数量是否一致。
- 检查单张图像和单个标签的 shape。

## 关键结论

`.npz` 可以理解为一个 NumPy 容器，里面用字符串 key 保存多个数组。

当前 `bloodmnist_128.npz` 中包含 6 个 key：

- `train_images`
- `train_labels`
- `val_images`
- `val_labels`
- `test_images`
- `test_labels`

检查结果：

- `train_labels.shape = (11959, 1)`
- 训练标签类别为 `[0 1 2 3 4 5 6 7]`，共 8 类
- `val_images.shape = (1712, 128, 128, 3)`
- `val_labels.shape = (1712, 1)`
- `val_images.shape[0] == val_labels.shape[0]` 为 `True`
- 单张验证图像 shape 为 `(128, 128, 3)`
- 单个验证标签 shape 为 `(1,)`

## 常见错误

1. 把属性当函数调用：

   `data.files` 是列表属性，不是函数，所以不能写成 `data.files()`。

2. 把 NumPy 模块函数误认为数组方法：

   `np.unique(train_labels)` 是正确写法；`train_labels.unique()` 对 NumPy array 不成立。

3. 字符串 key 写错：

   `.npz` 容器中要用准确的字符串 key，例如 `data["train_labels"]`。如果写成 `data["train_label"]` 会报 `KeyError`。

4. 混淆 PowerShell 和 Python：

   `import`、`hasattr(...)`、`callable(...)` 是 Python 语句，不能直接当作 PowerShell 命令执行。

5. 随机猜 API：

   遇到属性或方法不确定时，应优先使用 `type(...)`、`hasattr(...)`、`callable(...)` 和报错信息定位。

## Assessment 结果

Task Assessment：通过。

Independent：通过。

能力等级：

- Know：通过
- Understand：通过
- Implement：通过
- Independent：通过

Debug 能力评价：

基本通过。能够读懂并修复 `AttributeError`、`TypeError`、`KeyError`、`NameError` 等常见错误，但仍需继续训练“属性 / 方法 / 模块函数”和“PowerShell / Python 环境”的区分。
