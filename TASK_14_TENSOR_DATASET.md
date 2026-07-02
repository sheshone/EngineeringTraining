# Task 14: Tensor Dataset

## 目标

本 Task 的目标是让 Dataset 的 `__getitem__` 返回训练更可用的样本格式：

```text
(image_tensor, label_int)
```

其中图像应为 PyTorch Tensor，格式为 `CHW`，dtype 为 `float32`，像素范围约为 `0~1`。标签暂时返回普通 Python `int`。

本阶段仍不继承 `torch.utils.data.Dataset`，不写 DataLoader，不写 batch，不写模型，也不训练。

## 我实现了什么

正式脚本：

- `src/tensor_medmnist_dataset.py`

实现内容：

- 加载 `bloodmnist_128.npz`
- 读取 `train_images` 和 `train_labels`
- 定义 `transform_image(image)` 处理单张图像
- 定义 `TensorMedMNISTDataset`
- 在 `__getitem__(idx)` 中只处理第 `idx` 个样本
- 返回 `(image_tensor, label_int)`

## 图像转换流程

单张原始图像：

```text
NumPy image: (128, 128, 3), uint8, 0~255
```

在 `transform_image(image)` 中依次执行：

1. `/ 255.0`

   把像素范围缩放到约 `0~1`。

2. `torch.from_numpy(...)`

   把 NumPy array 转为 PyTorch Tensor。

3. `permute(2, 0, 1)`

   把 `HWC` 改为 `CHW`。

4. `.float()`

   把 Tensor 转为 `torch.float32`。

最终图像：

```text
torch.Size([3, 128, 128]), torch.float32
```

## 标签处理

原始标签：

```text
label.shape = (1,)
```

例如：

```text
[7]
```

使用：

```python
int(label[0])
```

得到普通 Python 整数：

```text
7
```

这样更符合分类任务中“类别编号”的含义。

## 关键结论

`__getitem__` 的职责是按索引返回一个样本，而不是每次转换整个数据集。

正确流程是：

```text
取 self.images[idx]
取 self.labels[idx]
只转换这一张 image
只处理这一个 label
返回 (image_tensor, label_int)
```

不能在每次 `__getitem__` 中转换整个 `self.images`，否则每取一个样本都会重复处理 11959 张图像，严重浪费资源。

## 常见错误

1. 每次 `__getitem__` 转换整个数据集。

   应该先取单张图像，再转换单张图像。

2. 混淆单张图像和整批图像的 `permute`。

   - 单张图像：`(H, W, C) -> (C, H, W)`，使用 `permute(2, 0, 1)`
   - 整批图像：`(N, H, W, C) -> (N, C, H, W)`，使用 `permute(0, 3, 1, 2)`

3. 忘记 `.float()`。

   `/255.0` 后从 NumPy 转到 Tensor 时常得到 `float64`，训练中通常需要 `float32`。

4. 标签也做归一化。

   label 是类别 ID，不是像素强度，不能 `/255.0`。

5. 直接返回 shape `(1,)` 的标签数组。

   分类任务中通常更需要类别编号，例如 `7`，而不是 `[7]`。

## Assessment 结果

Task Assessment：通过。

Independent：通过。

能力等级：

- Know：通过
- Understand：通过
- Implement：通过
- Independent：通过

Debug 能力评价：

基本通过。能够修复路径转义、构造函数参数、API 拼写、解包顺序和 dtype 问题。仍需继续训练单样本转换与整批转换的区别。
