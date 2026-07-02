import pathlib
import numpy as np
import torch

path = pathlib.Path("MedMNIST_Blood_Path_Organ_128/bloodmnist_128.npz")
data = np.load(path)
train_images, train_labels = data["train_images"], data["train_labels"]

def transform_image(image):
    normalized_image = image / 255.0
    tensorized_image = torch.from_numpy(normalized_image)
    permuted_image = tensorized_image.permute(2, 0, 1).float()
    return permuted_image

class TensorMedMNISTDataset():
    def __init__(self, images, labels):
        if len(images) != len(labels):
            raise ValueError("images and labels must have same length")
        self.images, self.labels = images, labels
    
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        image, label = self.images[idx], self.labels[idx]
        transformed_image = transform_image(image)
        return transformed_image, int(label[0])

dataset = TensorMedMNISTDataset(train_images, train_labels)
image, label = dataset[0]

print("dataset length:", len(dataset))
print("image shape:", image.shape)
print("image dtype:", image.dtype)
print("image min:", image.min())
print("image max:", image.max())
print("label:", label)
print("label type:", type(label))

data.close()