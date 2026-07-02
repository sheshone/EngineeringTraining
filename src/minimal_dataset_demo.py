class SimpleDataset():
    def __init__(self, images, labels):
        if len(images) != len(labels):
            raise ValueError("images and labels must have same length")
        self.images = images
        self.labels = labels
    def __len__(self):
        return len(self.images)
    def __getitem__(self, idx):
        return self.images[idx], self.labels[idx]

images = ["image0", "image1", "image2"]
labels = [0, 1, 0]
dataset = SimpleDataset(images, labels)
print(len(dataset), dataset[0], dataset[1])
