import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
])

train_dataset = datasets.CIFAR10(root = './data', train = True, download = True, transform = transform)
test_dataset = datasets.CIFAR10(root = './data', train = False, download = True, transform = transform)

train_loader = DataLoader(train_dataset, batch_size = 128, shuffle = True, num_workers = 0)
test_loader = DataLoader(test_dataset, batch_size = 128, shuffle = False, num_workers = 0)

def nin_block(in_channels, out_channels, kernel_size, strides, padding):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, kernel_size, strides, padding),
        nn.ReLU(),
        nn.Conv2d(out_channels, out_channels, kernel_size = 1),
        nn.ReLU(),
        nn.Conv2d(out_channels, out_channels, kernel_size = 1),
        nn.ReLU()
    )

class NiN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nin_block(3, 96, kernel_size = 5, strides = 1, padding = 2),    #96*32*32
            nn.MaxPool2d(2, stride = 2),#96*16*16
            nin_block(96, 256, kernel_size = 3, strides = 1, padding = 1),  #256*16*16
            nn.MaxPool2d(2, stride = 2),
            nin_block(256, 384, kernel_size = 3, strides = 1, padding = 1),
            nn.MaxPool2d(2, stride = 2),
            nn.Dropout(0.5),
            nin_block(384, 10, kernel_size = 3, strides = 1, padding = 1),
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten()
        )
    def forward(self, x):
        return self.net(x)

model = NiN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr = 0.001)

for epoch in range(10):
    model.train()
    total_loss = 0
    for img, label in train_loader:
        optimizer.zero_grad()
        outputs = model(img)
        loss = criterion(outputs, label)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for img, label in test_loader:
            outputs = model(img)
            _, predicted = torch.max(outputs, dim = 1)
            total += label.size(0)
            correct += (predicted == label).sum().item()

    acc = correct / total
    print(f"Epoch {epoch + 1:2d} | Loss: {total_loss / len(train_loader):.4f} | Test Acc: {acc:.4f}")

torch.save(model.state_dict(), r"D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\NiN\\nin_cifar10.pth")