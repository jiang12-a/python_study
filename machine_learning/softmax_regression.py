import torch
import torch.nn as nn   #67
import torch.optim as optim #优化器
import numpy as np
import matplotlib.pyplot as plt
import os
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#生成数据
np.random.seed(42)
K = 3  # 类别数
d = 2  # 特征维度
n_per_class = 100

centers = np.array([[4, 4], [-2, 2], [0, -2]])
X_list, y_list = [], []
for i in range(K):
    Xi = np.random.uniform(-5,5,(n_per_class, d)) + centers[i]
    X_list.append(Xi)
    y_list.append(np.full(n_per_class, i))

X_np = np.vstack(X_list).astype(np.float32)  # (300, 2)
y_np = np.concatenate(y_list).astype(np.int64)  # (300,)
X = torch.from_numpy(X_np)
y = torch.from_numpy(y_np)

#定义画布
x_line = np.linspace(X_np[:, 0].min() , X_np[:, 0].max() , 300)
y_line = np.linspace(X_np[:, 1].min() , X_np[:, 1].max() , 300)
xx, yy = np.meshgrid(x_line, y_line)

grid_np = np.c_[xx.ravel(), yy.ravel()].astype(np.float32)  #(90000,2)
grid_tensor = torch.from_numpy(grid_np)

#定义模型
# nn.Linear内部自带权重 W 和偏置 b，计算的是 X @ W.T + b
model = nn.Linear(in_features = d, out_features = K)
# 损失函数：输入原始 logits，内部自动做softmax，再算负对数似然。
criterion = nn.CrossEntropyLoss()
# 优化器：随机梯度下降
optimizer = optim.SGD(model.parameters(), lr = 0.01)

epochs = 500
losses = []

for epoch in range(epochs):
    # 1.前向传播：计算z = Wx + b
    logits = model(X)

    # 2.计算损失
    loss = criterion(logits, y)
    losses.append(loss.item())

    # 3.反向传播与更新参数
    optimizer.zero_grad()  # 清空上一步的残余梯度
    loss.backward()
    optimizer.step()  #更新w，b

    if epoch % 100 == 0:
        print(f"epoch={epoch}, loss:{loss.item():.4f}")
        with torch.no_grad():
            grid_logits = model(grid_tensor)    #shape为(90000,3)
            Z = torch.argmax(grid_logits, dim=1).numpy().reshape(300,300)

        fig, ax = plt.subplots(figsize=(6,5))
        ax.contourf(xx, yy, Z, alpha=0.25, cmap="viridis")
        colors = ["tab:red", "tab:green", "tab:blue"]
        for k in range(K):
            ax.scatter(X_np[y_np == k, 0], X_np[y_np == k, 1], s=15,
                            color=colors[k], label=f"class {k}")
        ax.set_title(f"决策边界 epoch={epoch}")
        ax.legend()
        ax.grid(alpha=0.3)
        plt.tight_layout()
        plt.savefig("D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\figures\\"f"boundary_epoch_{epoch}.png", dpi=200)
        plt.close()


plt.figure(figsize=(6,4))
plt.plot(losses)
plt.xlabel("epoch")
plt.ylabel("loss")
plt.title("交叉熵损失下降曲线")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig( "D:\\PyCharm\\pychram\\Python_Base_Study\\machine_learning\\figures\\""loss_curve.png", dpi=200)
plt.show()






#     if epoch % 100 == 0:
#         print(f"最终损失:{losses[-1]:.4f}")
#
# fig, axes = plt.subplots(1, 2, figsize=(12, 6))
# #损失曲线
# axes[0].plot(losses)
# axes[0].set_xlabel("epoch")
# axes[0].set_ylabel("loss")
# axes[0].set_title("交叉熵损失下降曲线")
# axes[0].grid(alpha=0.3)
# #决策边界
# xx, yy = np.meshgrid(
#     np.linspace(X_np[:, 0].min() - 1, X_np[:, 0].max() + 1, 300),
#     np.linspace(X_np[:, 1].min() - 1, X_np[:, 1].max() + 1, 300)
# )
# grid_np = np.c_[xx.ravel(), yy.ravel()].astype(np.float32)
# grid_tensor = torch.from_numpy(grid_np)
#
# with torch.no_grad():
#     grid_logits = model(grid_tensor)
#     Z = torch.argmax(grid_logits, dim=1).numpy().reshape(xx.shape)
#
# axes[1].contourf(xx, yy, Z, alpha=0.25, cmap="viridis")
# colors = ["tab:red", "tab:green", "tab:blue"]
# for k in range(K):
#     axes[1].scatter(X_np[y_np == k, 0], X_np[y_np == k, 1], s=15,
#                     color=colors[k], label=f"class {k}")
# axes[1].set_title("决策边界与样本")
# axes[1].legend()
# axes[1].grid(alpha=0.3)
#
# plt.tight_layout()
# plt.show()
