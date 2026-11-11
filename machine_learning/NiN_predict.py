import torch
import torch.nn as nn
from PIL import Image
from torchvision import transforms
import os
import glob

# 自动GPU/CPU
device = torch.device("cpu")

transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.4914, 0.4822, 0.4465],
        std=[0.2023, 0.1994, 0.2010]
    )
])

def nin_block(in_channels, out_channels, kernel_size, strides, padding):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, kernel_size, strides, padding),
        nn.ReLU(),
        nn.Conv2d(out_channels, out_channels, kernel_size = 1), nn.ReLU(),
        nn.Conv2d(out_channels, out_channels, kernel_size = 1), nn.ReLU()
    )

class NiN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nin_block(3, 96, kernel_size = 5, strides = 1, padding = 2),
            nn.MaxPool2d(2, stride = 2),
            nin_block(96, 256, kernel_size = 3, strides = 1, padding = 1),
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
model.load_state_dict(torch.load(r"D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\nin_cifar10.pth", map_location=device))
model.eval()

classes = [
    "飞机", "汽车", "鸟", "猫", "鹿",
    "狗", "青蛙", "马", "船", "卡车"
]
THRESHOLD = 0.55

def predict_folder(folder_path):
    img_paths = glob.glob(os.path.join(folder_path, "*"))
    for img_path in img_paths:
        filename = os.path.basename(img_path)
        try:
            img = Image.open(img_path).convert("RGB")
            img = transform(img).unsqueeze(0)
            with torch.no_grad():
                out = model(img)
                probs = torch.softmax(out, dim = 1)
                max_prob, pred = torch.max(probs, 1)
                max_prob_val = max_prob.item()
                pred_idx = pred.item()

            class_name = classes[pred_idx]
            if max_prob_val < THRESHOLD:
                result = f"未知类别(最接近：{class_name}，最高概率仅为{max_prob_val * 100:.2f}%)"
            else:
                result = f"{class_name} (置信度：{max_prob_val * 100:.2f}%)"
            print(f"{filename:<20} | {result}")

        except Exception as e:
            print(f"{filename:<20} | 图片读取失败")

if __name__ == "__main__":
    test_folder = r"D:\\PyCharm\\pychram\\Python_Base_Study\\Cat_Dog_Classification\\test_folder"
    predict_folder(test_folder)