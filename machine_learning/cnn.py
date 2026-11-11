import torch
import torch.nn as nn
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

torch.manual_seed(30)

# ================= 1. 造图像数据 =================
# 1024 个样本，1个通道，长宽为 28x28
x = torch.randn(1024, 1, 28, 28)
# 随便定个规律：根据左上角 [0, 0, 0] 的像素值正负来分类（回归任务，输出 1 个数）
t = x[:, 0, 0, 0].unsqueeze(1)

idx = torch.randperm(1024)
x_train, t_train = x[idx[:380]], t[idx[:380]]
x_test, t_test = x[idx[380:]], t[idx[380:]]


# ================= 2. 构建卷积网络 =================
def build_cnn(input_channel, output_dim):
    return nn.Sequential(
        nn.Conv2d(input_channel, 8, kernel_size=3, padding=1),
        nn.LeakyReLU(),
        nn.MaxPool2d(2),

        nn.Conv2d(8, 16, kernel_size=3, padding=1),
        nn.LeakyReLU(),
        nn.MaxPool2d(2),

        nn.Flatten(),  # 关键：拉平特征图

        nn.Linear(16 * 7 * 7, 64),
        nn.LeakyReLU(),
        nn.Dropout(0.2),
        nn.Linear(64, output_dim)
    )


# 构造模型（输入通道是 1）
model = build_cnn(input_channel=1, output_dim=1)

# CNN 的初始化
for m in model.modules():
    if isinstance(m, (nn.Conv2d, nn.Linear)):
        nn.init.kaiming_normal_(m.weight)

criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)  # 换成 Adam 更稳

# ================= 3. 训练并记录 =================
epoch_list = []
train_loss_list = []
test_loss_list = []

# 记录第一层卷积核的权重范数
w1_list = []

for epoch in range(100):
    model.train()
    optimizer.zero_grad()

    output = model(x_train)
    loss = criterion(output, t_train)
    loss.backward()
    optimizer.step()

    model.eval()
    with torch.no_grad():
        test_output = model(x_test)
        test_loss = criterion(test_output, t_test)

    epoch_list.append(epoch + 1)
    train_loss_list.append(loss.item())
    test_loss_list.append(test_loss.item())

    # 注意：这里记录的是 Conv2d 的权重
    w1_list.append(model[0].weight.norm().item())

    if epoch % 20 == 0:
        print(f"epoch:{epoch + 1} , train loss:{loss.item():.4f} , test loss:{test_loss.item():.4f}")

# ================= 4. 绘图 =================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax1.plot(epoch_list, train_loss_list, color="red", label="train loss")
ax1.plot(epoch_list, test_loss_list, color="blue", label="test loss")
ax1.set_title("LOSS 随训练轮次变化 (CNN)")
ax1.set_xlabel("epoch")
ax1.set_ylabel("loss")
ax1.legend()
ax1.grid(alpha=0.2)

# 这里画的是第一层卷积的权重范数
ax2.plot(epoch_list, w1_list, label="Conv1 Weight Norm", linewidth=2, color="green")
ax2.set_title("第一层卷积核权重范数变化")
ax2.set_xlabel("epoch")
ax2.set_ylabel("weight norm")
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()