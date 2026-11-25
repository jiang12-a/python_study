import os
import json
import numpy as np
from PIL import Image
from torchvision import transforms
from torch.utils.data import DataLoader
from tqdm import tqdm
from train import Food101Dataset

def compute_mean_std(dataset, batch_size=32, num_workers=4):
    # 只做 ToTensor，不做 Normalize，尺寸缩放到 224 保持一致
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),   # 自动转成 [0,1] 的 float tensor
    ])
    dataset.transform = transform

    loader = DataLoader(dataset, batch_size=batch_size,
                        shuffle=False, num_workers=num_workers)

    n_pixels = 0          # 累计像素总数 (N*H*W)
    sum_ = np.zeros(3)    # 每个通道的像素和
    sum_sq = np.zeros(3)  # 每个通道的平方和

    for imgs, _ in tqdm(loader):
        # imgs: (B, 3, H, W) 取值 [0,1]
        imgs = imgs.numpy()
        n_pixels += imgs.shape[0] * imgs.shape[2] * imgs.shape[3]
        # 按通道求和
        sum_ += imgs.sum(axis=(0, 2, 3))
        sum_sq += (imgs ** 2).sum(axis=(0, 2, 3))

    mean = sum_ / n_pixels
    std = np.sqrt(sum_sq / n_pixels - mean ** 2)
    return mean, std


if __name__ == '__main__':
    base = r"D:\PyCharm\pychram\Python_Base_Study\machine_learning\ResNet\Food101"
    train_root = os.path.join(base, "test")
    train_json = os.path.join(base, "test", "test.json")

    ds = Food101Dataset(root_dir=train_root, json_file=train_json)
    mean, std = compute_mean_std(ds)

    print("Mean:", mean)
    print("Std:", std)