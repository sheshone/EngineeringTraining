# Review Pool（长期复习池）

## 使用规则

- Task Assessment：当前 Task 完成后立即进行，验证理解、实现、Debug 和独立完成能力。
- Review：与完成时间隔开，用于防止遗忘，不与 Assessment 混用。
- 每天开始新 Task 前安排 5～15 分钟 Warm-up。
- Warm-up 不抽取当天刚完成的 Task。
- 优先抽取曾经答错、尚不稳定或较久未复习的知识。
- 到期项目是抽题候选，不要求一天复习全部到期内容。
- Review 压力过大时，减少抽题数量并延长稳定知识的间隔。

## 当前复习池

| Task | 完成日期 | 最近长期 Review | 下次候选日期 | 当前优先级 | 重点知识 |
|---|---|---|---|---|---|
| Task 1：开发环境与命令行 | 2026-06-28 | 尚未进行 | 2026-06-30 | 中 | 当前目录、解释器路径、CPU/CUDA 构建、PowerShell/Linux 命令 |
| Task 2：初始化 Git 仓库 | 2026-06-28 | 尚未进行 | 2026-06-30 | 高 | 仓库边界、`.git`、exFAT、`safe.directory`、工作区/暂存区/历史 |
| Task 3：仓库文件分类 | 2026-06-28 | 尚未进行 | 2026-06-30 | 中 | 源码与权重、数据、缓存、凭据、许可证、外部存储 |
| Task 4：最小 `.gitignore` | 2026-06-28 | 2026-06-29 | 2026-07-02 | 中 | 根目录锚定、目录规则、已跟踪文件、忽略不等于删除 |
| Task 5：选择性暂存 | 2026-06-29 | 尚未进行 | 2026-06-30 | 高 | 工作目录/暂存区/历史、选择性 `add`、`diff --cached`、快照更新 |
| Task 6：第一次 Git 提交 | 2026-06-29 | 尚未进行 | 2026-06-30 | 高 | commit/push、哈希、HEAD/分支、amend、log/reflog、提交前验证 |
| Task 7：小而完整的增量提交 | 2026-06-29 | 尚未进行 | 2026-06-30 | 高 | 增量提交流程、暂存区检查、`-- <path>`、`--oneline`、失败后停止 Debug |
| Task 8：创建最小项目结构 | 2026-06-30 | 尚未进行 | 2026-07-01 | 高 | `src/`、`notebooks/`、`outputs/`、`.gitkeep`、空目录、PowerShell 文件操作 |
| Task 9：最小环境检查脚本 | 2026-06-30 | 尚未进行 | 2026-07-01 | 高 | Python 导入、`sys.executable`、PyTorch 版本、`pathlib`、当前工作目录与脚本路径 |

## 跨 Task 高优先级薄弱点

| 知识点 | 来源 | 最近表现 | 下次候选日期 |
|---|---|---|---|
| 删除前核对路径和影响范围 | Task 2、Task 4 | 曾误把删除目标写成整个项目根目录 | 2026-06-30 |
| 命令与参数精确拼写 | Task 1、Task 2、Task 4、Task 5 | 能自行修正，但错误频率仍高 | 2026-06-30 |
| 不同命令的参数归属 | Task 4、Task 5 | 曾把 Git 参数用于 PowerShell 命令 | 2026-06-30 |
| 执行前等待 Review | Task 4、Task 5 | 曾在要求暂停时提前执行 | 2026-06-30 |
| 模型源码、权重与环境文件 | Task 3 | 新场景中最终正确，仍需间隔复习 | 2026-07-01 |
| 检查失败后停止而非绕过 | Task 6 | 首次练习跳过暂存检查，第二次已改正 | 2026-06-30 |
| 提交前完整验证流程 | Task 7 | 功能已能完成，但独立 Assessment 刚过线 | 2026-06-30 |
| `--` 路径分隔符与长选项拼写 | Task 7 | 曾写成 `--"test.txt"` 和 `-oneline`，已修正 | 2026-06-30 |
| PowerShell 文件操作模板 | Task 8 | 能纠错后写出，独立稳定性仍偏弱 | 2026-07-01 |
| 空目录、`.gitkeep` 与 ignore 的关系 | Task 8 | 最初概念混淆，修正后通过 | 2026-07-01 |
| Python 导入与关键字拼写 | Task 9 | 曾把 `import` 写成 `improt`，能够定位并修正 | 2026-07-01 |
| 当前工作目录与脚本所在目录 | Task 9 | 最初误认为相对路径天然相对项目根目录，修正后通过 | 2026-07-01 |

## Review 记录

### 2026-06-29：Task 4

- 形式：次日闭卷抽查与实际清理。
- 结果：`.gitignore` 核心概念保持良好。
- 新发现：删除命令目标路径发生高风险错误。
- 调整：忽略规则延长至 3 天后；删除路径安全加入次日高优先级 Warm-up。

## Assessment 与 Review 状态

- Task 1：Assessment 已通过，已进入 Review Pool。
- Task 2：Assessment 已通过，已进入 Review Pool。
- Task 3：Assessment 已通过，已进入 Review Pool。
- Task 4：Assessment 已通过，已进入 Review Pool；已完成一次长期 Review。
- Task 5：Assessment 已通过，已进入 Review Pool。
- Task 6：Assessment 已通过，已进入 Review Pool。
- Task 7：Assessment 已通过，已进入 Review Pool。
- Task 8：Assessment 已通过，已进入 Review Pool。
- Task 9：Assessment 已通过，已进入 Review Pool。
### Task 10：Inspect NPZ Dataset

- 完成日期：2026-07-01
- Assessment：通过，已进入 Review Pool
- Review 优先级：高
- 重点知识：
  - `.npz` 是 NumPy 容器，使用字符串 key 访问数组。
  - `data.files` 是属性，不是函数，不能写成 `data.files()`。
  - `np.unique(array)` 是 NumPy 模块函数，不是 `array.unique()`。
  - `val_images.shape = (N, H, W, C)`，本任务中为 `(1712, 128, 128, 3)`。
  - `val_images.shape[0] == val_labels.shape[0]` 只能证明数量一致，不能证明一一对应一定正确。
  - Python 语句不能直接在 PowerShell 中执行；调试时要区分 shell 环境和 Python 环境。
- 薄弱点：
  - 属性 / 方法 / 模块函数的区分仍需复习。
  - API 不确定时要优先使用 `type`、`hasattr`、`callable`，不要随机猜。
### Task 11：Inspect Image Pixel Range

- 完成日期：2026-07-01
- Assessment：通过，已进入 Review Pool
- Review 优先级：高
- 重点知识：
  - `train_images.shape = (N, H, W, C)`，本任务中为 `(11959, 128, 128, 3)`。
  - `train_images[0]` 会去掉样本维度，得到单张图像 `(128, 128, 3)`。
  - `image[0, 0]` 是一个像素的 RGB 三个通道值，shape 为 `(3,)`。
  - `uint8` 表示无符号 8 位整数，范围是 `0~255`。
  - `image / 255.0` 会产生浮点数组，通常用于把像素缩放到 `0~1`。
  - 归一化改变像素值和 dtype，不改变图像 shape。
- 薄弱点：
  - `data.files` 与 `data["train_images"]` 的区别仍需复习。
  - 原地操作 `image /= 255` 和非原地操作 `image = image / 255` 的区别需要继续训练。
### Task 12：NumPy Image to PyTorch Tensor CHW

- 完成日期：2026-07-02
- Assessment：通过，已进入 Review Pool
- Review 优先级：高
- 重点知识：
  - NumPy 图像常见格式是 `HWC`，本任务中为 `(128, 128, 3)`。
  - PyTorch 单张 CNN 图像常用 `CHW`，本任务中为 `(3, 128, 128)`。
  - `torch.from_numpy(...)` 只转换容器，不会自动改变维度顺序。
  - `permute(2, 0, 1)` 把原来的 `C` 维从最后移动到最前。
  - `/255.0` 改变像素值范围，`permute` 改变维度顺序，`.float()` 改变 dtype。
  - 深度学习中通常使用 `float32`，因为精度通常够用且更省内存、计算更快、和模型权重 dtype 更一致。
- 薄弱点：
  - `data.files` 与 `data["train_images"]` 的区别仍需抽查。
  - 正式脚本应减少 `hasattr/callable/help` 等临时调试输出。
### Task 13：Minimal Dataset

- 完成日期：2026-07-02
- Assessment：通过，已进入 Review Pool
- Review 优先级：高
- 重点知识：
  - `len(dataset)` 会调用 `dataset.__len__()`。
  - `dataset[idx]` 会调用 `dataset.__getitem__(idx)`。
  - Dataset 的职责是按索引返回一个样本 `(image, label)`。
  - `idx` 是样本索引，不是类别。
  - `__len__` 应返回 `len(self.images)`，不能写 `len(self)`。
  - `__init__` 中应先检查 `len(images) == len(labels)`，再保存到 `self.images` 和 `self.labels`。
  - 真实 MedMNIST 第 0 个样本中，image shape 为 `(128, 128, 3)`，label shape 为 `(1,)`。
- 薄弱点：
  - 类属性赋值、局部变量与对象属性的关系需要继续复习。
  - `__len__` 中递归调用 `len(self)` 的错误需要抽查。
  - 类名和变量名不应相同。
### Task 14：Tensor Dataset

- 完成日期：2026-07-02
- Assessment：通过，已进入 Review Pool
- Review 优先级：高
- 重点知识：
  - `__getitem__(idx)` 应只处理第 `idx` 个样本，不应每次转换整个数据集。
  - 单张图像转换流程：`/255.0 -> torch.from_numpy -> permute(2,0,1) -> .float()`。
  - 单张图像 `permute(2,0,1)`：`(H,W,C) -> (C,H,W)`。
  - 整批图像换序思路：`(N,H,W,C) -> (N,C,H,W)`，对应 `permute(0,3,1,2)`。
  - label 是类别 ID，不做归一化。
  - `int(label[0])` 把 shape `(1,)` 的标签数组转换为普通类别整数。
- 薄弱点：
  - Windows 路径字符串中的反斜杠转义，例如 `\b`。
  - 单样本转换和整批转换的维度顺序仍需抽查。
  - Dataset 返回值解包顺序应保持 `(image, label)`。
### Task 15：PyTorch Dataset

- 完成日期：2026-07-02
- Assessment：通过，已进入 Review Pool
- Review 优先级：高
- 重点知识：
  - 继承 `torch.utils.data.Dataset` 后仍然要自己实现 `__len__` 和 `__getitem__`。
  - PyTorch Dataset 基类不能直接代表你的具体数据集，必须实例化自己的子类。
  - Dataset 负责按索引返回单个样本，DataLoader 负责批量取样、shuffle、组 batch，`nn.Module` 负责模型前向计算。
  - 继承 Dataset 不会自动完成归一化、Tensor 转换或 `permute`。
  - `isinstance(dataset, Dataset)` 为 `True` 表示自定义数据集对象也是 PyTorch Dataset 类型。
- 薄弱点：
  - 长度检查不能误写成 `len(images) != len(images)`。
  - Dataset / DataLoader / nn.Module 的职责边界需要长期复习。
  - 正式错误信息应清楚说明原因，不应使用 `"!!!"`。
### Task 16：Minimal DataLoader

- 完成日期：2026-07-03
- Assessment：通过，已进入 Review Pool
- Review 优先级：高
- 重点知识：
  - Dataset 返回单个样本，DataLoader 把多个样本组合成 batch。
  - 单样本 image shape 为 `[3,128,128]`，batch images shape 为 `[4,3,128,128]`。
  - 单样本 label 是 Python `int`，batch labels shape 为 `[4]`，dtype 为 `torch.int64`。
  - `len(dataset)` 是样本总数，`batch_size` 是每个 batch 的样本数，`len(dataloader)` 是 batch 总数。
  - `iter(dataloader)` 创建迭代器，`next(...)` 取下一个 batch。
  - `shuffle=False` 时第一个 batch 对应样本索引 `0,1,2,3`。
- 薄弱点：
  - 容易混淆 `len(dataloader)` 和 `batch_size`。
  - 类方法中应使用 `self.images`，不要误用外部全局变量。
  - DataLoader 不负责归一化、permute 或训练。
