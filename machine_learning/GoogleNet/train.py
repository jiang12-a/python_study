import os
import sys
import torch
import torch.nn as nn
from torchvision import transforms, datasets
import torch.optim as optim
from torch.utils.data import random_split, Dataset
from tqdm import tqdm
from model import GoogLeNet

# 数据集下载链接：http://download.tensorflow.org/example_images/flower_photos.tgz

torch.manual_seed(0)
generator = torch.Generator().manual_seed(0)

class DatasetFromSubset(Dataset):
    def __init__(self, subset, transform=None):
        self.subset = subset
        self.transform = transform

    def __getitem__(self, index):
        x, y = self.subset[index]
        if self.transform:
            x = self.transform(x)
        return x, y

    def __len__(self):
        return len(self.subset)

train_transform = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

val_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

image_path = os.path.abspath("./FlowersImages")
assert os.path.exists(image_path), f"{image_path} 路径不存在！"

dataset = datasets.ImageFolder(root = image_path)

total_size = len(dataset)
train_size = int(0.8 * total_size)
val_size = total_size - train_size
train_subset, val_subset = random_split(dataset, [train_size, val_size],generator = generator)

train_dataset = DatasetFromSubset(train_subset, transform = train_transform)
val_dataset = DatasetFromSubset(val_subset, transform = val_transform)

train_num = len(train_dataset)
val_num = len(val_dataset)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size = 32, shuffle = True)
val_loader = torch.utils.data.DataLoader(val_dataset,batch_size = 32, shuffle = False)

net = GoogLeNet(num_classes = 5, aux_logits = True, init_weights = True)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr = 0.0003)

best_acc = 0.0
train_steps = len(train_loader)

for epoch in range(30):
    # train
    net.train()
    running_loss = 0.0
    train_bar = tqdm(train_loader, file=sys.stdout)
    for step, data in enumerate(train_bar):
        images, labels = data
        optimizer.zero_grad()
        logits, aux_logits2, aux_logits1 = net(images)
        loss0 = criterion(logits, labels)
        loss1 = criterion(aux_logits1, labels)
        loss2 = criterion(aux_logits2, labels)
        loss = loss0 + loss1 * 0.3 + loss2 * 0.3
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        train_bar.desc = "train epoch[{}/{}] loss:{:.3f}".format(epoch + 1 , 30 , loss)

    # val
    net.eval()
    acc = 0.0
    with torch.no_grad():
        val_bar = tqdm(val_loader, file=sys.stdout)
        for val_data in val_bar:
            val_images, val_labels = val_data
            outputs = net(val_images)
            _ , predict_y = torch.max(outputs, dim = 1)
            acc += torch.eq(predict_y, val_labels).sum().item()

    val_accurate = acc / val_num
    print('[epoch %d] train_loss: %.3f  val_accuracy: %.3f' %(epoch + 1, running_loss / train_steps, val_accurate))

    if val_accurate > best_acc:
        best_acc = val_accurate
        torch.save(net.state_dict(), "D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\GoogleNet\\googleNet.pth")