import os
import glob
import torch
from PIL import Image
from torchvision import transforms
from model import ResNet


BASE_DIR = r"D:\PyCharm\pychram\Python_Base_Study\machine_learning\ResNet"
WEIGHTS_PATH = os.path.join(BASE_DIR, "best.pth")
TRAIN_IMAGES_DIR = os.path.join(BASE_DIR, "Food101", "test", "images")
TEST_FOLDER = os.path.join(BASE_DIR, "predict_folder")


def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize((0.545, 0.445, 0.344), (0.229, 0.226, 0.225))
    ])

    # 获取文件夹下所有图片
    all_files = [f for f in os.listdir(TRAIN_IMAGES_DIR) if f.endswith('.jpg')]

    unique_classes = sorted(list(set([f.rsplit('_', 1)[0] for f in all_files])))

    class_indict = {str(i): name for i, name in enumerate(unique_classes)}

    model = ResNet(num_classes=101).to(device)

    weights_dict = torch.load(WEIGHTS_PATH, map_location=device)
    model.load_state_dict(weights_dict, strict=True)
    model.eval()

    img_paths = glob.glob(os.path.join(TEST_FOLDER, "*.jpg")) + \
                glob.glob(os.path.join(TEST_FOLDER, "*.png"))

    for img_path in img_paths:
        filename = os.path.basename(img_path)
        try:
            img = Image.open(img_path).convert("RGB")
            img_tensor = transform(img).unsqueeze(0).to(device)

            with torch.no_grad():
                out = model(img_tensor)
                probs = torch.softmax(out, dim=1)
                max_prob, pred = torch.max(probs, 1)

                max_prob_val = max_prob.item()
                pred_idx = pred.item()

            class_name = class_indict[str(pred_idx)].replace('_', ' ')

            result = f"{class_name:<30} (置信度: {max_prob_val * 100:.2f}%)"
            print(f"{filename:<30} | {result}")

        except Exception as e:
            print(f"{filename:<30} | 预测失败: {e}")


if __name__ == "__main__":
    main()