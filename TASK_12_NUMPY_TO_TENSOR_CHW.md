# Task 12: NumPy Image to PyTorch Tensor CHW

## 目标

本 Task 的目标是把一张 NumPy 图像从 `HWC` 格式转换为 PyTorch CNN 常用的 `CHW` Tensor 格式。

本阶段只处理一张图像，不写 Dataset、DataLoader、模型或训练循环。

## 我检查了什么

- 从 `bloodmnist_128.npz` 中读取 `train_images`。
- 取第 0 张训练图像。
- 将原始 `uint8` 图像除以 `255.0`，归一化到约 `0~1`。
- 使用 `torch.from_numpy(...)` 将 NumPy array 转为 PyTorch Tensor。
- 检查 Tensor 的 shape、dtype、min、max。
- 使用 `permute(2, 0, 1)` 将 Tensor 从 `HWC` 转为 `CHW`。
- 使用 `.float()` 将 Tensor 从 `float64` 转为 `float32`。

## 关键结论

原始单张图像：

- NumPy shape：`(128, 128, 3)`
- dtype：`uint8`
- 含义：`H, W, C`

归一化后：

- shape 不变：`(128, 128, 3)`
- dtype 变为浮点类型
- 像素范围约为 `0~1`

转成 Tensor 后：

- shape 仍然是 `torch.Size([128, 128, 3])`
- `torch.from_numpy(...)` 不会自动改变维度顺序

使用 `permute(2, 0, 1)` 后：

- shape 变为 `torch.Size([3, 128, 128])`
- 含义：`C, H, W`
- dtype 和数值范围不因 `permute` 改变

使用 `.float()` 后：

- dtype 变为 `torch.float32`
- shape 仍然是 `torch.Size([3, 128, 128])`

## 底层理解

NumPy 图像常见格式是 `HWC`，也就是高度、宽度、通道。

PyTorch 的 `Conv2d` 通常使用 `NCHW`。对于单张图像，去掉 batch 维度后就是 `CHW`。

`permute(2, 0, 1)` 的含义是重新排列维度：

- 原第 2 维：通道 `C`
- 原第 0 维：高度 `H`
- 原第 1 维：宽度 `W`

因此 `(H, W, C)` 会变成 `(C, H, W)`。

## 常见错误

1. 以为 `torch.from_numpy(...)` 会自动把 `HWC` 变成 `CHW`。

   它只转换数据容器，不改变维度顺序。

2. 混淆 `/255.0`、`permute` 和 `.float()` 的作用。

   - `/255.0` 改变像素值范围
   - `permute(2, 0, 1)` 改变维度顺序
   - `.float()` 改变 Tensor dtype

3. 忘记转成 `float32`。

   PyTorch 模型权重通常是 `float32`，输入也应保持一致。

4. 混淆通道数和类别数。

   图像通道数是 RGB 的 `3`，类别数来自标签，不来自图像 shape 的最后一维。

5. 忘记关闭 `.npz` 文件。

   使用 `np.load(...)` 后应在脚本结尾调用 `data.close()`。

## Assessment 结果

Task Assessment：通过。

Independent：通过。

能力等级：

- Know：通过
- Understand：通过
- Implement：通过
- Independent：通过

Debug 能力评价：

通过。能够独立完成 NumPy 到 Tensor 的转换，并正确使用 `permute(2, 0, 1)` 和 `.float()`。仍需继续减少正式脚本中的临时调试输出，并持续复习 `data.files` 与 `data["key"]` 的区别。
