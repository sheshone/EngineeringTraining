from torch.utils.data import Dataset
import pathlib
import torch
import numpy as np

def transform(image, label):
    normalized_image = image / 255.0
    tensorized_image = torch.from_numpy(normalized_image)
    permuted_image = tensorized_image.permute(2, 0, 1).float()
    transformed_label = int(label[0])
    return permuted_image, transformed_label

class TensorMedMNISTDataset(Dataset):

    def __init__(self, images, labels):
        if len(images) != len(labels):
            raise ValueError("images and labels must have same length")
        self.images = images
        self.labels = labels
    
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        image, label = self.images[idx], self.labels[idx]
        return transform(image, label)
    
path = pathlib.Path("MedMNIST_Blood_Path_Organ_128/bloodmnist_128.npz")
data = np.load(path)
train_images, train_labels = data["train_images"], data["train_labels"]
dataset = TensorMedMNISTDataset(train_images, train_labels)
image, label = dataset[0]

print("dataset is instance of Dataset",isinstance(dataset, Dataset))
print("length of dataset",len(dataset))
print("shape of image",image.shape)
print("dtype of image",image.dtype)
print("min of image",image.min())
print("max of image",image.max())
print("label",label)
print("dtype of label",type(label))

data.close()