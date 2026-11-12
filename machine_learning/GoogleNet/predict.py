import torch
from PIL import Image
from torchvision import transforms
import os
import glob
from model import GoogLeNet

#测试集下载链接：https://www.kaggle.com/datasets/imsparsh/flowers-dataset?resource=download

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

model = GoogLeNet(num_classes = 5, aux_logits = False)

# 模型权重路径
weights_path = r"D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\GoogleNet\\googleNet.pth"

# 剔除训练时保存的辅助分类器权重
weights_dict = torch.load(weights_path)
del_list = ["aux1.fc2.weight", "aux1.fc2.bias", "aux2.fc2.weight", "aux2.fc2.bias"]
new_weights_dict = {}
for k, v in weights_dict.items():
    if k not in del_list:
        new_weights_dict[k] = v
model.load_state_dict(new_weights_dict, strict = False)

model.eval()

class_indict = {
    "0": "daisy",
    "1": "dandelion",
    "2": "roses",
    "3": "sunflowers",
    "4": "tulips"
}

def predict_folder(folder_path):
    img_paths = glob.glob(os.path.join(folder_path, "*"))

    for img_path in img_paths:
        filename = os.path.basename(img_path)
        try:
            img = Image.open(img_path).convert("RGB")
            img = transform(img).unsqueeze(0)

            with torch.no_grad():
                out = model(img)
                probs = torch.softmax(out, dim = 1)  # 对类别维度求 softmax

                max_prob, pred = torch.max(probs, 1)
                max_prob_val = max_prob.item()
                pred = pred.item()

            # 获取类别名称
            class_name = class_indict[str(pred)]

            result = f"{class_name} (置信度：{max_prob_val * 100:.2f}%)"
            print(f"{filename:<20} | {result}")

        except Exception as e:
            print(f"{filename:<20} | 图片读取或预测失败")

if __name__ == "__main__":
    test_folder = r"D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\GoogleNet\\test"
    predict_folder(test_folder)
