import torch
import torch.nn as nn

class TinyCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear = nn.Linear(3 * 128 * 128, 8)

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear(x)
        return logits

model = TinyCNN()
images = torch.randn(4, 3, 128, 128)
logits = model(images)

print("images shape:", images.shape)
print("logits shape", logits.shape)
