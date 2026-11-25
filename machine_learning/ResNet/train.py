import os
import json
import torch
import time
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from model import ResNet

log_path = r"D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\ResNet\\train_log.txt"

class Food101Dataset(Dataset):
    def __init__(self, root_dir, json_file, transform = None):
        self.root_dir = root_dir
        self.transform = transform
        self.image_paths = []
        self.labels = []
        self.class_to_idx = {}
        new_labels = []

        with open(json_file, "r", encoding = "utf-8") as f:
            data = json.load(f)

        for item in data.get("images", []):
            file_name = item["file_name"]

            # rsplit从右往左切，然后按照 "_" 将其换成两个字符串
            cls_name = file_name.rsplit('_', 1)[0]

            # 拼接完整图片路径：root_dir + /images/ + 文件名
            img_path = os.path.join(root_dir, "images", file_name)

            self.image_paths.append(img_path)
            self.labels.append(cls_name)

        unique_classes = sorted(list(set(self.labels)))     #set()自动去重
        for i, cls_name in enumerate(unique_classes):   #enumerate()将列表中每个元素及其索引返回
            self.class_to_idx[cls_name] = i
        self.classes = unique_classes

        for cls_name in self.labels:
            number = self.class_to_idx[cls_name]
            new_labels.append(number)
        self.labels = new_labels

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

    with open(log_path, "w", encoding = "utf-8") as f:
        f.write(f"训练开始时间：{time.strftime('%Y-%m-%d %H:%M:%S')} ")

    train_transform = transforms.Compose([
        transforms.Resize(256),  # 短边变 256，长边等比例缩小
        transforms.RandomCrop(224),  #随机裁剪 224x224，能增强泛化能力
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(10),
        transforms.ColorJitter(brightness = 0.2 , contrast = 0.2),
        transforms.ToTensor(),
        transforms.Normalize((0.545, 0.445, 0.344), (0.229, 0.226, 0.225))
    ])

    val_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.RandomCrop(224),
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
        log_text = f"Epoch [{epoch + 1}/{epochs}] | Loss: {total_loss / len(train_loader):.4f} | Val Acc: {acc:.4f}\n"
        print(log_text.strip())
        with open(log_path, "a", encoding = "utf-8") as f:
            f.write(log_text)

        if acc > best_acc:
            best_acc = acc
            save_dict = {
                "epoch": epoch + 1,
                "best_acc": best_acc,
                "model_state_dict": model.state_dict()
            }
            torch.save(save_dict, r"D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\ResNet\\best.pth")

if __name__ == '__main__':
    main()