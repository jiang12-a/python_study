import json
from pathlib import Path
import os

root_dir = ("D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\ResNet\\Food101\\test")
path = Path("D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\ResNet\\Food101\\test\\test.json")

test = path.read_text()
data = json.loads(test)
images_list = data["images"]

for img in images_list[:]:
    print(f"序号:{img['id']}")
    print(f"菜名:{img['file_name']}")
    print(f"图片大小:{img['width']} * {img['height']}")
# with open(path, "r", encoding = "utf-8") as f:
#     data = json.load(f)
# # print(data)
# # print(data["images"][:3])
# for i in data.get("images", []):
#     file_name = i["file_name"]
#     cls_name = file_name.rsplit('_', 1)[0]
#     img_path = os.path.join(root_dir, "images", file_name)
#     print(img_path)