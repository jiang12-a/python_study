import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import random

random.seed(42)
torch.manual_seed(42)
generator = torch.Generator().manual_seed(42)

device = torch.device("cpu")
data_dir = "D:\\PyCharm\\pychram\\Python_Base_Study\\Cat_Dog_Classification\\PetImages"

#计算数据集的均值（mean）和标准差（std）
calc_transform = transforms.Compose([
    transforms.Resize((64,64)),
    transforms.ToTensor()
])

dataset = datasets.ImageFolder(data_dir , transform = calc_transform)
dataloader = DataLoader(dataset , batch_size = 100)
# 只需要一个通道维度为3的容器，用来累加和
mean = torch.zeros(3)
std = torch.zeros(3)
total_images = 0

for images , labels in dataloader:
    batch_size = images.size(0) # images 的 shape 是 (batch_size, 3, 64, 64)
    images = images.view(batch_size, images.size(1), -1)    # 把图片展平成 (batch_size, 3, H*W)，方便按通道计算
    mean += images.mean(2).sum(0)
    std += images.std(2).sum(0)
    total_images += batch_size

mean /= total_images
std /= total_images

transform = transforms.Compose([
    transforms.Resize((64 , 64)),
    transforms.ToTensor(),
    transforms.Normalize(mean = mean.tolist(), std = std.tolist())
])

dataset = datasets.ImageFolder(data_dir , transform = transform)
# 划分训练集和验证集（80% 用于训练，20% 用于验证）
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size] , generator = generator)

train_loader = DataLoader(train_dataset, batch_size = 32, shuffle = True)
val_loader = DataLoader(val_dataset, batch_size = 32, shuffle = False)

#CNN
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size = 3, padding = 1)  # 输入3通道RGB
        self.conv2 = nn.Conv2d(32, 64, kernel_size = 3, padding = 1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 16 * 16, 128)
        self.fc2 = nn.Linear(128, 2)  # 最后输出2类：猫、狗
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(-1, 64 * 16 * 16)  # 展平
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

model = SimpleCNN()

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr = 0.001)

for epoch in range(10):
    model.train()
    running_loss = 0.0
    for images, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    # 验证集评估
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in val_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(
        f"Epoch {epoch + 1} / 10, Loss: {running_loss / len(train_loader):.4f}, Val Acc: {100 * correct / total:.2f}%")

torch.save(model.state_dict(), r"D:\\PyCharm\\pychram\\Python_Base_Study\\Cat_Dog_Classification\\cat_dog_cnn.pth")