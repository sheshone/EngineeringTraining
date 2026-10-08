# Task 18：最小 nn.Module 前向传播

## 目标

- 理解创建层、保存层和调用层的区别。
- 使用 `nn.Module` 定义最小模型。
- 理解 `model(images)` 与 `forward(images)` 的关系。
- 验证 batch 输入与 logits 输出的 shape。

## 核心结果

- 输入：`[B, C, H, W] = [4, 3, 128, 128]`
- `Flatten` 后：`[4, 49152]`
- `Linear(49152, 8)` 后：`[4, 8]`
- `[4, 8]` 表示一个 batch 中有 4 个样本，每个样本得到 8 个类别分数。
- logits 是原始类别分数，不是概率。

## 关键概念

```python
self.flatten = nn.Flatten()
```

右侧创建层对象，左侧把层保存为模型属性。

```python
x = self.flatten(x)
```

调用已经保存的层处理输入。

```python
model(images)
```

通过 `nn.Module.__call__` 进入模型的 `forward(images)`。

## 准确命名

当前结构只有 `Flatten + Linear`，属于线性分类器，不是真正的 CNN；真正的 CNN 至少需要卷积层，例如 `nn.Conv2d`。

## Task Assessment

- 概念解释：通过。
- 独立实现：通过。
- 独立运行结果：

```text
logits size torch.Size([2, 8])
images shape torch.Size([2, 3, 128, 128])
```

结论：已完成，进入 Review Pool（复习池）。

## 薄弱点

- 容易把一个 batch 中的样本数误称为 batch 数量。
- 需要继续巩固层的创建、属性赋值与层调用之间的区别。
- `Flatten` 默认保留 batch 维度。
