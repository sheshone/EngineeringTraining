# Task 17: Batch Sanity Check

## 目标

本 Task 的目标是在训练前检查 DataLoader 输出的 batch 是否满足后续 CNN 和分类 loss 的基本要求。

本阶段不写模型、不写 loss、不写 optimizer、不训练，只做 batch 检查。

## 我实现了什么

正式脚本：

- `src/batch_sanity_check.py`

实现内容：

- 加载 `bloodmnist_128.npz`
- 定义继承 `torch.utils.data.Dataset` 的 Dataset
- 使用 DataLoader 创建 batch
- 取第一个 batch
- 检查 images 和 labels 的 shape、dtype、device、数值范围
- 检查 labels 的类别范围
- 检查 batch 是否符合 CNN 和分类任务的基本输入要求

## 当前 batch 结果

本任务中：

```text
batch_size = 4
num_classes = 8
```

第一个 batch：

```text
images.shape = torch.Size([4, 3, 128, 128])
images.dtype = torch.float32
images.device = cpu
labels.shape = torch.Size([4])
labels.dtype = torch.int64
labels.device = cpu
labels = tensor([7, 3, 6, 6])
```

labels 范围：

```text
min label = 3
max label = 7
legal range = 0 ~ 7
```

## 关键结论

CNN batch 输入通常是：

```text
[B, C, H, W]
```

本任务中：

```text
[4, 3, 128, 128]
```

含义：

- `4`：一个 batch 中有 4 个样本
- `3`：每张图像有 RGB 三个通道
- `128`：高度
- `128`：宽度

如果错误地给成 `[4,128,128,3]`，PyTorch `Conv2d` 会按 `[N,C,H,W]` 解释，把 `128` 误认为 channel，把 `3` 误认为 width，语义完全错位。

## labels 的要求

分类任务中，label 是类别索引，不是连续数值。

对于 8 分类：

```text
合法类别编号：0,1,2,3,4,5,6,7
```

因此必须满足：

```text
0 <= label < num_classes
```

本任务中 `num_classes = 8`，所以合法范围是 `0~7`。

labels 应该是：

```text
shape = [B]
dtype = torch.int64 / torch.long
```

原因：

- 每个样本只需要一个正确类别索引
- `CrossEntropyLoss` 通常期望 target 是一维类别索引
- 类别索引用整数，不能用 float 表达

## device 检查

训练时，参与同一次计算的 Tensor 通常必须在同一个 device 上。

如果模型在 CUDA，但 images 或 labels 在 CPU，可能报错：

```text
Expected all tensors to be on the same device
```

当前本机 PyTorch 是 CPU 版本，因此 images 和 labels 都在：

```text
cpu
```

## `.item()` 的作用

`labels.min()` 返回的是单元素 Tensor：

```text
tensor(3)
```

`labels.min().item()` 会取出 Python 数字：

```text
3
```

普通 Python 条件判断和日志中，用 `.item()` 可读性更好。

注意：`.item()` 只能用于单元素 Tensor，不能直接用于整个 labels batch。

## 常见错误

1. 混淆 batch 和 channel。

   `[4,3,128,128]` 中 `4` 是一个 batch 中的样本数，不是 4 个 batch；`3` 是 RGB 通道，不是 3 个模型。

2. 把 `[B,H,W,C]` 喂给 PyTorch `Conv2d`。

   PyTorch `Conv2d` 默认需要 `[B,C,H,W]`。

3. labels 仍然是 `[B,1]`。

   普通单标签多分类更适合 `[B]`。

4. labels 是 float。

   分类 label 是类别索引，应该是整数类型。

5. `num_classes` 写成类别数组。

   `np.unique(train_labels)` 是类别列表；类别数应写成 `len(np.unique(train_labels))`。

6. 对多元素 Tensor 直接 `.item()`。

   `.item()` 只能用于单元素 Tensor，例如 `labels.min().item()`。

## Assessment 结果

Task Assessment：通过。

Independent：通过。

能力等级：

- Know：通过
- Understand：通过
- Implement：通过
- Independent：通过

Debug 能力评价：

基本通过。能够独立完成 batch sanity check，并修复 `num_classes`、`.item()` 和 labels 范围检查问题。需要继续复习 batch/channel、分类 label 作为索引、以及 `[B,C,H,W]` 的语义。
