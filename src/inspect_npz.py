import numpy as np
import pathlib
file_path = pathlib.Path("./MedMNIST_Blood_Path_Organ_128/bloodmnist_128.npz")
print(file_path.exists())
print(file_path.is_file())
data = np.load(file_path)
print(data.files)
train_labels = data["train_labels"]
print(train_labels.shape)
print(train_labels.dtype)
unique_labels = np.unique(train_labels) 
print(unique_labels)
print(len(unique_labels))
val_images = data["val_images"] 
print(val_images.shape)
print(val_images.dtype)
val_labels = data["val_labels"] 
print(val_labels.shape)
print(val_images.shape[0] == val_labels.shape[0])
print(val_images[0].shape)
print(val_labels[0].shape)
data.close()