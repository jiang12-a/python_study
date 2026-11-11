import torch
import torch.nn as nn
from PIL import Image
from envs.ml_env.Lib.fileinput import filename
from torchvision import transforms
import os
import glob

transform = transforms.Compose([
    transforms.Resize((64 , 64)),
    transforms.ToTensor(),
    transforms.Normalize(mean = [0.4883076250553131, 0.455269992351532, 0.4170190691947937], std = [0.2172398567199707, 0.21250371634960175, 0.21277625858783722])
])

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size = 3, padding = 1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size = 3, padding = 1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 16 * 16, 128)
        self.fc2 = nn.Linear(128, 2)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(-1, 64 * 16 * 16)
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

model = SimpleCNN()
model.load_state_dict(torch.load(r"D:\\PyCharm\\pychram\\Python_Base_Study\\Cat_Dog_Classification\\cat_dog_cnn.pth"))
model.eval()

THRESHOLD = 0.8

def predict_folder(folder_path):
    img_paths = glob.glob(os.path.join(folder_path, "*"))

    for img_path in img_paths:
        filename = os.path.basename(img_path)

        try:
            img = Image.open(img_path).convert("RGB")
            img = transform(img).unsqueeze(0)

            with torch.no_grad():
                out = model(img)    #out.shape = (1,2) (批次大小，类别数)
                probs = torch.softmax(out, dim = 1)     #dim = 1，代表对类别进行softmax，每个样本的概率之和为1

                max_prob , pred = torch.max(probs, 1)
                max_prob_val = max_prob.item()
                pred = pred.item()

            if pred == 0:
                class_name = "猫"
            else:
                class_name = "狗"

            if max_prob_val < THRESHOLD:
                result =  f"未知类别(最接近：{class_name} , 最高概率仅为{max_prob_val * 100:.2f}%)"
            else:
                result =  f"{class_name} (置信度：{max_prob_val * 100:.2f}%)"
            # print(f"{img_path} | {result}")
            print(f"{filename:<20} | {result}")

        except Exception as e:
            # print(f"{img_path} | 图片读取失败")
            print(f"{filename:<20} | 图片读取失败")

if __name__ == "__main__":
    test_folder = "D:\\PyCharm\\pychram\\Python_Base_Study\\Cat_Dog_Classification\\test_folder"
    predict_folder(test_folder)






# def predict_img(img_path):
#     img = Image.open(img_path).convert("RGB")
#     img_tensor = transform(img).unsqueeze(0)
#     with torch.no_grad():
#         out = model(img_tensor)
#         # pred = torch.argmax(out, dim = 1).item()
#
#         probs = torch.softmax(out , dim = 1)
#
#         max_prob , pred = torch.max(probs, 1)
#         max_prob_val = max_prob.item()
#         pred = pred.item()
#
#     if pred == 0:
#         class_name = "猫"
#     else:
#         class_name = "狗"
#
#     if max_prob_val < THRESHOLD:
#         return f"未知类别(最接近：{class_name} , 最高概率仅为{max_prob_val * 100:.2f}%)"
#
#     return f"{class_name} (置信度：{max_prob_val * 100:.2f}%)"
#
# if __name__ == "__main__":
#     result = predict_img(r'D:\\other6.jpg')
#     print("预测结果：", result)


