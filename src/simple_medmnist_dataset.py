import pathlib
import numpy as np

path = pathlib.Path("MedMNIST_Blood_Path_Organ_128/bloodmnist_128.npz")
data = np.load(path)
train_images = data["train_images"]
train_labels = data["train_labels"]

class SimpleMedMNISTDataset():
    def __init__(self, images, labels):
        if len(images) != len(labels):
            raise ValueError("images and labels must have same length")
        self.images = images
        self.labels = labels
        
    def __len__(self):
        return len(self.images)
    def __getitem__(self, idx):
        return self.images[idx], self.labels[idx]
    
dataset = SimpleMedMNISTDataset(train_images, train_labels)
image, label = dataset[0]
print("dataset length:", len(dataset))
print("image shape:", image.shape)
print("label shape:", label.shape)
print("image dtype:", image.dtype)
print("label dtype:", label.dtype)

data.close()