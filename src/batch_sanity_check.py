import pathlib
import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader


path = pathlib.Path("MedMNIST_Blood_Path_Organ_128/bloodmnist_128.npz")
data = np.load(path)
train_images, train_labels = data["train_images"], data["train_labels"]


def transformed_image(image):
    normalized_image = image / 255.0
    tensorized_image = torch.from_numpy(normalized_image)
    permuted_image = tensorized_image.permute(2, 0, 1).float()
    return permuted_image

def transformed_label(label):
    return int(label[0])


class MedDataset(Dataset):
    
    def __init__(self, images, labels):
        if len(images) != len(labels):
            raise ValueError("quantity match error")
        self.images, self.labels = images, labels
    
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, index):
        image, label = self.images[index], self.labels[index]
        return transformed_image(image), transformed_label(label)

dataset = MedDataset(train_images, train_labels)
dataloader = DataLoader(dataset, batch_size = 4, shuffle = False)
images, labels = next(iter(dataloader))
num_classes = len(np.unique(train_labels))

print("length of dataset and batch number:",len(dataset),len(dataloader))
print("shape of images:",images.shape,
      "\ndtype of images:" ,images.dtype,
      "\ndevice of images:", images.device, 
      "\nmin of images:",images.min(), 
      "\nmax of images",images.max())

print("labels:",labels,
      "\nshape of labels:", labels.shape, 
      "\ndtype of labels:",labels.dtype, 
      "\ndevice of labels:",labels.device, 
      "\nnum of classes:",num_classes)
print("min of labels:", labels.min())
print("max of labels:", labels.max())
print("dim of images is 4:", images.ndim == 4)
print("dtype of images is float32:", images.dtype == torch.float32)
print("dim of labels is 1:", labels.ndim == 1)
print("dtype of labels is int64:",labels.dtype == torch.int64)
label_range_ok = (labels.min().item() >= 0) and (labels.max().item() < num_classes)
print("value of labels is in range:", label_range_ok)
print("image channel is 3:",images.shape[1] == 3)
print("label is index:", labels.ndim == 1 and labels.dtype == torch.int64)
data.close()