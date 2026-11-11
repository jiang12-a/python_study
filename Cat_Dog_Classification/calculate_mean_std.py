import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

data_dir = r"D:\\PyCharm\\pychram\\Python_Base_Study\\Cat_Dog_Classification\\PetImages"

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

print(f"均值: {mean.tolist()}")
print(f"标准差: {std.tolist()}")
