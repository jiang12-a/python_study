import pandas as pd
from sklearn.datasets import fetch_openml

# 本地内置加载泰坦尼克数据集，不访问github
titanic = fetch_openml("titanic", version=1, as_frame=True)
df = titanic.frame

print("数据集行列：", df.shape)
print("\n每列缺失值数量：")
print(df.isnull().sum())
print("\n前5行数据：")
print(df.head())

# 导出成本地csv文件，以后就可以本地读取，不用再加载数据集
df.to_csv("D:\\PyCharm\\pychram\\Python_Base_Study\\data\\titanic.csv", index=False)

