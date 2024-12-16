# 项目名称

**作者**: 韩文强/中国传媒大学/hanwenqiang_qd@126.com

本项目演示了如何加载与查看 `.bin` 格式的模型权重文件，并且对模型参数进行简单的检查与打印。本 README 提供了一个简单的使用说明和示例代码片段，帮助你快速上手。

## 功能特性

- **加载 PyTorch 模型权重**：从 `.bin` 文件中加载模型的 `state_dict`。
- **打印模型层名称和参数形状**：方便快速了解模型的结构和参数规模。
- **可扩展的加载方式**：可根据需要适配 Hugging Face Transformers 模型或其他框架的权重文件。

## 环境依赖

- Python 3.x
- PyTorch (若使用 PyTorch 的 `.bin` 文件)
- Transformers (若使用 Hugging Face 的模型权重)
- TensorFlow / Keras (若需要加载 `.h5` 或检查点格式文件，不过 `.bin` 文件需自行转换为对应格式)

## 快速开始

### 加载 PyTorch `.bin` 权重文件

下面的示例演示了如何使用 PyTorch 加载一个 `.bin` 文件，其中存储了模型的 `state_dict`。加载后，我们打印了所有参数名称及其形状。

```python
import torch

# 假设你有一个名为 model.bin 的权重文件
model_weights = torch.load('model.bin')

# 打印所有层的名称和张量形状
for name, param in model_weights.items():
    print(f"Layer: {name}, Shape: {param.shape}")
