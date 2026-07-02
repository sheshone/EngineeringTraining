import pathlib
import numpy as np
import torch

path = pathlib.Path("./MedMNIST_Blood_Path_Organ_128/bloodmnist_128.npz")
data = np.load(path)
train_images = data["train_images"]
image =train_images[0]
norm_image = image / 255.0
tensor_image = torch.from_numpy(norm_image)
print("NumPy image shape:", image.shape)
print("NumPy image dtype:", image.dtype)
print("norm NumPy image shape", norm_image.shape)
print("norm NumPy image dtype", norm_image.dtype)
print("norm NumPy image min", norm_image.min())
print("norm NumPy image max", norm_image.max())
print("tensor image shape:", tensor_image.shape)
print("tensor image dtype:", tensor_image.dtype)
print("tensor image max", tensor_image.max())
print("tensor image min", tensor_image.min())
data.close()
tensor_chw = tensor_image.permute(2, 0, 1)
print("tensor chw shape:", tensor_chw.shape)
print("tensor chw dtype:", tensor_chw.dtype)
print("tensor chw min:", tensor_chw.min())
print("tensor chw max:", tensor_chw.max())
tensor_chw = tensor_chw.float()
print("tensor chw shape:", tensor_chw.shape)
print("tensor chw dtype:", tensor_chw.dtype)
print("tensor chw min:", tensor_chw.min())
print("tensor chw max:", tensor_chw.max())