import os
import json
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from model import ResNet


class Food101Dataset(Dataset):
    def __init__(self, root_dir, json_file, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.image_paths = []
        self.labels = []

        # 1. 解析 JSON 文件
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 2. 遍历 JSON 中的 images 列表
        for item in data.get("images", []):
            file_name = item["file_name"]  # 例如: "apple_pie_003.jpg"

            # 提取类别名称：apple_pie_003.jpg -> apple_pie
            cls_name = file_name.rsplit('_', 1)[0]

            # 拼接完整图片路径：root_dir + /images/ + 文件名
            img_path = os.path.join(root_dir, "images", file_name)

            self.image_paths.append(img_path)
            self.labels.append(cls_name)

        # 3. 将字符串类别转换为数字索引 (0~100)
        unique_classes = sorted(list(set(self.labels)))
        self.class_to_idx = {cls_name: i for i, cls_name in enumerate(unique_classes)}
        self.classes = unique_classes

        # 4. 替换为数字标签
        self.labels = [self.class_to_idx[cls_name] for cls_name in self.labels]

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        label = self.labels[idx]
        img = Image.open(img_path).convert("RGB")
        if self.transform:
            img = self.transform(img)
        return img, label

def main():

    train_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(10),
        transforms.ColorJitter(brightness=0.2, contrast=0.2),
        transforms.ToTensor(),
        transforms.Normalize((0.545, 0.445, 0.344), (0.229, 0.226, 0.225))
    ])

    val_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize((0.545, 0.445, 0.344), (0.229, 0.226, 0.225))
    ])

    train_root = ("D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\ResNet\\Food101\\test")
    train_json = ("D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\ResNet\\Food101\\test\\test.json")

    val_root = ("D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\ResNet\\Food101\\val")
    val_json = ("D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\ResNet\\Food101\\val\\val.json")

    train_dataset = Food101Dataset(root_dir = train_root , json_file = train_json , transform = train_transform)
    val_dataset = Food101Dataset(root_dir = val_root , json_file = val_json , transform = val_transform)

    train_loader = DataLoader(train_dataset , batch_size = 32 , shuffle = True)
    val_loader = DataLoader(val_dataset , batch_size = 32 , shuffle = False)

    model = ResNet(num_classes = 101)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr = 0.05, momentum = 0.9)

    best_acc = 0.0
    epochs = 60

    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for img, label in train_loader:
            optimizer.zero_grad()
            outputs = model(img)
            loss = criterion(outputs, label)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        # 验证阶段
        model.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for img, label in val_loader:
                outputs = model(img)
                _, predicted = torch.max(outputs, dim = 1)
                total += label.size(0)
                correct += (predicted == label).sum().item()

        acc = correct / total
        print(f"Epoch [{epoch + 1}/{epochs}] | Loss: {total_loss / len(train_loader):.4f} | Val Acc: {acc:.4f}")

        if acc > best_acc:
            best_acc = acc
            torch.save(model.state_dict(), "D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\ResNet\\best.pth")

if __name__ == '__main__':
    main()