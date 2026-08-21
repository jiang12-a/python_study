import ortools
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
import os

# print("爬虫环境就绪")

url = "https://books.toscrape.com/"
response = requests.get(url)
# print("状态码：",response.status_code)
# print(response.text[:500])
html = response.text
soup = BeautifulSoup(html, "html.parser")
books = soup.find_all("article",class_="product_pod")

data_list = []
for book in books:
    book_name = book.find("h3").find("a")["title"]
    book_price = book.find("p",class_="price_color").text
    data_list.append({
        "书名":book_name,
        "价格":book_price
    })
df = pd.DataFrame(data_list)

# 获取当前脚本所在的 spider 文件夹路径
current_dir = os.path.dirname(__file__)
# 定位到项目根目录（spider 的上一级目录）
project_root = os.path.dirname(current_dir)
# 拼接出 data 文件夹的完整路径
data_dir = os.path.join(project_root, "data")
# 自动创建 data 文件夹，已存在也不会报错
os.makedirs(data_dir, exist_ok=True)
# 拼接完整的文件保存路径
save_path = os.path.join(data_dir, "图书数据.csv")
df = pd.DataFrame(data_list)
df.to_csv(save_path, index=False, encoding="utf-8-sig")


print("保存完成！共爬取",len(data_list),"本书")
time.sleep(10)