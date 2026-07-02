# Task 13: Minimal Dataset

## 目标

本 Task 的目标是理解 Dataset 的最小机制：`__len__` 和 `__getitem__`。

本阶段不使用 DataLoader、不写训练循环、不写 CNN，也暂时不继承 `torch.utils.data.Dataset`。先用普通 Python 类理解 Dataset 的核心行为。

## 我实现了什么

本 Task 写了两个脚本：

- `src/minimal_dataset_demo.py`：用假数据理解 Dataset 机制。
- `src/simple_medmnist_dataset.py`：用真实 MedMNIST NumPy 数据验证同样机制。

最小 Dataset 类包含：

- `__init__(self, images, labels)`：接收图像和标签，并检查数量是否一致。
- `__len__(self)`：返回样本数量。
- `__getitem__(self, idx)`：根据索引返回一个样本 `(image, label)`。

## 关键结论

`len(dataset)` 背后调用的是：

```python
dataset.__len__()
```

`dataset[0]` 背后调用的是：

```python
dataset.__getitem__(0)
```

在真实 MedMNIST 数据中：

- `len(dataset) = 11959`
- `image.shape = (128, 128, 3)`
- `label.shape = (1,)`
- `image.dtype = uint8`
- `label.dtype = uint8`

`image, label = dataset[0]` 表示：

- 从 `self.images[0]` 取第 0 张图像
- 从 `self.labels[0]` 取第 0 个标签
- 两者组成一个样本对

## 为什么要检查长度一致

Dataset 默认认为 `images[idx]` 和 `labels[idx]` 是同一个样本的图像和标签。

如果图像数量和标签数量不一致，后续可能出现：

- 图像没有对应标签
- 标签没有对应图像
- 索引越界
- 训练时图像和标签错配

因此应在 `__init__` 中先检查：

```python
len(images) == len(labels)
```

确认合法后再保存到 `self.images` 和 `self.labels`。

## 常见错误

1. 在 `__len__` 中写 `len(self)`。

   这会导致无限递归，因为 `len(self)` 又会调用 `self.__len__()`。

2. `__getitem__` 返回整个数据集。

   Dataset 的职责是按索引返回一个样本，而不是每次返回全部数据。

3. 把 `idx` 当成类别。

   `idx` 是样本索引，不是 label。

4. 类名和变量名相同。

   例如 `class dataset` 后又写 `dataset = dataset(...)`，会覆盖类名，不利于后续复用。

5. 先保存坏数据再检查。

   更清晰的习惯是先检查输入合法性，再保存到对象属性。

## Assessment 结果

Task Assessment：通过。

Independent：通过。

能力等级：

- Know：通过
- Understand：通过
- Implement：通过
- Independent：通过

Debug 能力评价：

通过。能够根据 `AttributeError`、`RecursionError` 和 Dataset 输出结果修正代码。需要继续巩固 `__len__` / `__getitem__` 的触发机制，以及类名、对象名、属性名之间的区别。
