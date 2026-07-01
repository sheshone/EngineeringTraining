import numpy as np
import pathlib
file_path = pathlib.Path("./MedMNIST_Blood_Path_Organ_128/bloodmnist_128.npz")
data = np.load(file_path)

train_images = data["train_images"]
print("train_images shape:",train_images.shape
      ,"\nsingle image shape:", train_images[0].shape
      ,"\nsingle image dtype:", train_images[0].dtype
      ,"\nsingle image min:", train_images[0].min()
      ,"\nsingle image max:", train_images[0].max()
      ,"\nsingle image pixel:", train_images[0][0,0]
      ,"\nsingle image pixel shape:", train_images[0][0, 0].shape)
image_float = train_images[0] / 255.0
print("Normalized dtype:", image_float.dtype)
print("Normalized min:", image_float.min())
print("Normalized max:", image_float.max())
print("a Normalized pixel:", image_float[0, 0])
print("Normalized shape:", image_float.shape)
data.close()