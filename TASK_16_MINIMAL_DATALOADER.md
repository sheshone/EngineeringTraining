# Task 16: Minimal DataLoader

## 目标

本 Task 的目标是理解 DataLoader 如何把 Dataset 返回的单个样本组合成 batch。

本阶段不写模型、不写 loss、不写 optimizer、不训练，只观察 DataLoader 的输出形态。

## 我实现了什么

正式脚本：

- `src/minimal_dataloader.py`

实现内容：

- 加载 `bloodmnist_128.npz`
- 定义继承 `torch.utils.data.Dataset` 的 `MedMNISTDataset`
- `__getitem__` 返回单个样本：
  - image：`torch.Size([3, 128, 128])`, `torch.float32`, 像素范围约 `0~1`
  - label：Python `int`
- 创建 DataLoader：
  - `batch_size=4`
  - `shuffle=False`
- 使用 `next(iter(dataloader))` 取第一个 batch
- 打印 batch 的 shape、dtype、min、max 和 labels

## 关键结论

Dataset 返回单个样本：

```text
image: torch.Size([3, 128, 128])
label: int
```

DataLoader 组合成 batch 后：

```text
images: torch.Size([4, 3, 128, 128])
labels: torch.Size([4])
```

本任务输出：

```text
len(dataset) = 11959
len(dataloader) = 2990
images.dtype = torch.float32
labels.dtype = torch.int64
```

`labels.dtype` 是 `torch.int64`，因为 Dataset 返回 Python `int`，DataLoader 默认 collate 会把多个 int 组成一个整数 Tensor。这个格式适合后续分类任务常用的 `CrossEntropyLoss`。

## len(dataset)、batch_size、len(dataloader)

三者含义不同：

- `len(dataset)`：样本总数，本任务是 `11959`
- `batch_size`：每个 batch 最多包含多少样本，本任务是 `4`
- `len(dataloader)`：batch 总数，本任务是 `2990`

原因：

```text
11959 = 4 * 2989 + 3
```

默认 `drop_last=False`，最后剩下的 3 个样本也会组成一个 batch，因此：

```text
len(dataloader) = 2989 + 1 = 2990
```

## iter 和 next

```python
loader_iter = iter(dataloader)
images, labels = next(loader_iter)
```

含义：

- `iter(dataloader)` 创建一个 DataLoader 迭代器
- `next(loader_iter)` 取出下一个 batch

常见训练循环：

```python
for images, labels in dataloader:
    ...
```

本质上也是不断从 DataLoader 迭代器中取下一个 batch，直到取完。

## 常见错误

1. 把 `len(dataloader)` 误认为 batch size。

   `len(dataloader)` 是 batch 数量，不是每个 batch 的样本数。

2. 以为 DataLoader 会自动归一化或 `permute`。

   DataLoader 主要负责批量取样、shuffle、组 batch、可并行加载。图像转换逻辑仍然在 Dataset 中。

3. 以为 DataLoader 会训练模型。

   DataLoader 只提供数据，不负责模型计算和反向传播。

4. 在 Dataset 类内部误用外部全局变量。

   类方法中应使用 `self.images` 和 `self.labels`，不要写成外部变量 `images`、`labels`。

5. 混淆 label 单样本和 label batch。

   Dataset 返回一个 `int` label；DataLoader 会把多个 label 组合成 `torch.Size([batch_size])` 的 Tensor。

## Assessment 结果

Task Assessment：通过。

Independent：通过。

能力等级：

- Know：通过
- Understand：通过
- Implement：通过
- Independent：通过

Debug 能力评价：

基本通过。能够独立完成 Dataset 到 DataLoader 的最小链路，并修复类内部误用全局变量的问题。仍需继续复习 `len(dataset)`、`batch_size`、`len(dataloader)` 三者区别。
