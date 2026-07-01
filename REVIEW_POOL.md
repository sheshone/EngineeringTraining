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
