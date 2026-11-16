import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split
from model import ResNet

def main():
    # 训练集：加入随机裁剪和颜色抖动，提高泛化能力
    train_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomRotation(15),  # 随机旋转15度
        transforms.ColorJitter(brightness = 0.2, contrast = 0.2),  # 随机改变亮度和对比度
        transforms.ToTensor(),
        transforms.Normalize((0.3403, 0.3121, 0.3214), (0.2724, 0.2608, 0.2669))
    ])

    val_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize((0.3403, 0.3121, 0.3214), (0.2724, 0.2608, 0.2669))
    ])

    full_train_dataset = datasets.ImageFolder(
        root="D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\ResNet\\GTSRB\\Train",
        transform = train_transform
    )
    full_val_dataset = datasets.ImageFolder(
        root="D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\ResNet\\GTSRB\\Train",
        transform = val_transform
    )

    train_size = int(0.8 * len(full_train_dataset))
    val_size = len(full_train_dataset) - train_size
    generator = torch.Generator().manual_seed(42)
    train_dataset, _ = random_split(full_train_dataset, [train_size, val_size], generator = generator)
    _, val_dataset = random_split(full_val_dataset, [train_size, val_size], generator = generator)

    train_loader = DataLoader(train_dataset , batch_size = 64 , shuffle = True)
    val_loader = DataLoader(val_dataset , batch_size = 64 , shuffle = False)

    model = ResNet(num_classes = 43)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr = 0.01, momentum  = 0.9, weight_decay = 5e-4)
    # 学习率衰减：每过 10 个 epoch，学习率乘以 0.1
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)

    best_acc = 0.0
    for epoch in range(20):
        model.train()
        total_loss = 0
        for img, label in train_loader:
            optimizer.zero_grad()
            outputs = model(img)
            loss = criterion(outputs, label)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
        scheduler.step()

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
        print(f"Epoch [{epoch + 1}/{20}] | Loss: {total_loss / len(train_loader):.4f} | Test Acc: {acc:.4f}")

        if acc > best_acc:
            best_acc = acc
            torch.save(model.state_dict(), "D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\ResNet\\best.pth")
if __name__ == '__main__':
    main()