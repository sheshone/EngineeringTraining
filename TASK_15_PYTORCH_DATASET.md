# Task 15: PyTorch Dataset

## 目标

本 Task 的目标是把前面自己实现的 Dataset 类改成 PyTorch 标准 Dataset。

核心变化是继承：

```python
from torch.utils.data import Dataset
```

并定义：

```python
class TensorMedMNISTDataset(Dataset):
    ...
```

本阶段不写 DataLoader、不写 batch、不写模型、不训练。

## 我实现了什么

正式脚本：

- `src/pytorch_medmnist_dataset.py`

实现内容：

- 加载 `bloodmnist_128.npz`
- 读取 `train_images` 和 `train_labels`
- 定义继承 `torch.utils.data.Dataset` 的 `TensorMedMNISTDataset`
- 保留 `__len__` 和 `__getitem__`
- 在 `__getitem__` 中返回 `(image_tensor, label_int)`
- 检查 `isinstance(dataset, Dataset)` 是否为 `True`

## 关键结论

继承 `torch.utils.data.Dataset` 后，仍然需要自己实现：

```python
__len__
__getitem__
```

原因是 PyTorch 不知道你的数据在哪里、样本怎么取、图像怎么转换、标签怎么处理。

`Dataset`、`DataLoader`、`nn.Module` 的分工：

- `Dataset`：定义样本数量，以及如何按 `idx` 返回一个样本。
- `DataLoader`：基于 Dataset 批量取样、shuffle、组 batch、可并行加载。
- `nn.Module`：定义模型的前向计算。

## 当前输出格式

`dataset[0]` 返回：

```text
image: torch.Size([3, 128, 128]), torch.float32
label: int
```

其中 image 的处理流程仍然是：

```text
/255.0 -> torch.from_numpy -> permute(2,0,1) -> .float()
```

label 的处理流程是：

```text
label[0] -> int
```

## 常见错误

1. 以为继承 Dataset 后不需要写 `__len__` 和 `__getitem__`。

   实际上这两个方法仍然必须根据自己的数据定义。

2. 直接实例化 PyTorch 基类：

   ```python
   dataset = Dataset(train_images, train_labels)
   ```

   这是错误的。应该实例化自己写的子类：

   ```python
   dataset = TensorMedMNISTDataset(train_images, train_labels)
   ```

3. 以为继承 Dataset 会自动归一化、转 Tensor、permute。

   不会。这些转换逻辑仍然要写在自己的代码里。

4. 混淆 Dataset 和 DataLoader。

   Dataset 管“单个样本怎么取”，DataLoader 管“如何批量取样和组 batch”。

5. 长度检查写错。

   应检查：

   ```python
   len(images) == len(labels)
   ```

   不能误写成 `len(images) == len(images)`。

## Assessment 结果

Task Assessment：通过。

Independent：通过。

能力等级：

- Know：通过
- Understand：通过
- Implement：通过
- Independent：通过

Debug 能力评价：

基本通过。能够修复基类实例化错误、变量定义顺序、长度检查错误。仍需继续复习 Dataset / DataLoader / nn.Module 的职责边界。
