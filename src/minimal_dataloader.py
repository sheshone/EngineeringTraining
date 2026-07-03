import pathlib
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader

def transformed_image(image):
    normalized_image = image / 255.0
    tensorized_image = torch.from_numpy(normalized_image)
    permuted_image = tensorized_image.permute(2, 0, 1).float()
    return permuted_image

def transformed_label(label):
    return int(label[0])

class MedMNISTDataset(Dataset):
    def __init__(self, images, labels):
        if len(images) != len(labels):
            raise ValueError("images and labels must have same length")
        self.images = images
        self.labels = labels
    def __len__(self):
        return len(self.images)
    def __getitem__(self,idx):
        image = self.images[idx]
        label = self.labels[idx]
        return transformed_image(image), transformed_label(label)

path = pathlib.Path("MedMNIST_Blood_Path_Organ_128/bloodmnist_128.npz")
data = np.load(path)
train_images, train_labels = data["train_images"], data["train_labels"]
dataset = MedMNISTDataset(train_images, train_labels)
dataloader = DataLoader(dataset, batch_size = 4, shuffle = False)
images, labels = next(iter(dataloader))

print("length of dataset",len(dataset))
print("length of dataloader",len(dataloader))
print("shape of images",images.shape)
print("dtype of images",images.dtype)
print("min of images",images.min())
print("max of images",images.max())
print("labels", labels)
print("shape of labels",labels.shape)
print("dtype of labels",labels.dtype)

data.close()