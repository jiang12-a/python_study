import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset, random_split
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

class MLP(nn.Module):
    def __init__(self, input_dim, hidden_dims, output_dim):
        super(MLP, self).__init__()
        layers = []
        prev = input_dim
        for h in hidden_dims:
            layers.append(nn.Linear(prev, h))
            layers.append(nn.ReLU())
            layers.append(nn.Dropout(0.2))
            prev = h
        layers.append(nn.Linear(prev, output_dim))
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x)

np.random.seed(42)
torch.manual_seed(42)

# X = np.random.randn(1000, 64)
# y_onehot = np.zeros((1000,10))
# rand_label = np.random.randint(0,10,size=1000)
# y_onehot[np.arange(1000), rand_label] = 1
#
# X_tensor = torch.tensor(X, dtype=torch.float32)
# y_tensor = torch.tensor(np.argmax(y_onehot, axis=1), dtype=torch.long)
#
# dataset = TensorDataset(X_tensor, y_tensor)

X = np.random.randn(5000, 64)

# 之前是全部 64 个特征相加（太简单了，模型一秒学会）。
# 现在改成：只有前 4 个特征的和大于 0，标签才为 1。稍微增加一点点难度。
y_np = (X[:, :4].sum(axis=1) > 0).astype(int)

X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y_np, dtype=torch.long)

dataset = TensorDataset(X_tensor, y_tensor)

# 划分训练集、测试集
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_set, test_set = random_split(dataset, [train_size, test_size])

train_loader = DataLoader(train_set, batch_size=64, shuffle=True)
test_loader = DataLoader(test_set, batch_size=64, shuffle=False)

# 模型、损失、优化器
model = MLP(64, [64, 32], 2)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001,weight_decay=1e-4)

# 保存绘图数据
train_loss_list = []
test_loss_list = []
train_acc_list = []
test_acc_list = []

def calculate_loss_acc(loader):
    """计算整个数据集loss和准确率"""
    model.eval()
    total_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for bx, by in loader:
            logits = model(bx)
            loss = criterion(logits, by)
            total_loss += loss.item() * bx.shape[0]
            pred = torch.argmax(logits, dim=1)
            correct += (pred == by).sum().item()
            total += bx.shape[0]
    avg_loss = total_loss / total
    acc = correct / total
    return avg_loss, acc


epochs = 200
for epoch in range(epochs):
    # -------- 训练 --------
    model.train()
    train_total_loss = 0.0
    for batch_x, batch_y in train_loader:
        optimizer.zero_grad()
        output = model(batch_x)
        loss = criterion(output, batch_y)
        loss.backward()
        optimizer.step()
        train_total_loss += loss.item() * batch_x.shape[0]
    train_avg_loss = train_total_loss / len(train_set)

    # -------- 评估 --------
    test_avg_loss, test_acc = calculate_loss_acc(test_loader)
    _, train_acc = calculate_loss_acc(train_loader)

    train_loss_list.append(train_avg_loss)
    test_loss_list.append(test_avg_loss)
    train_acc_list.append(train_acc)
    test_acc_list.append(test_acc)

    if (epoch + 1) % 50 == 0:
        print(f"Epoch {epoch+1:2d} | TrainLoss:{train_avg_loss:.4f} | TestLoss:{test_avg_loss:.4f} | TrainAcc:{train_acc:.3f} | TestAcc:{test_acc:.3f}")


# ========== 可视化绘图 ==========
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 损失曲线
ax1.plot(train_loss_list, label="训练损失", color="#1f77b4")
ax1.plot(test_loss_list, label="测试损失", color="#ff7f0e")
ax1.set_xlabel("Epoch")
ax1.set_ylabel("Loss")
ax1.set_title("损失曲线")
ax1.legend()
ax1.grid(alpha=0.3)

# 准确率曲线
ax2.plot(train_acc_list, label="训练准确率", color="#1f77b4")
ax2.plot(test_acc_list, label="测试准确率", color="#ff7f0e")
ax2.set_xlabel("Epoch")
ax2.set_ylabel("Accuracy")
ax2.set_title("准确率曲线")
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("mlp_loss_acc.png", dpi=200)
plt.show()

# 预测函数
def mlp_predict(model, x_new_np):
    model.eval()
    x_tensor = torch.from_numpy(x_new_np.astype(np.float32))
    with torch.no_grad():
        logits = model(x_tensor)
        pred_y = torch.argmax(logits, dim=1)
    return pred_y.numpy()

# 测试预测
test_x = np.random.randn(5,64)
pred = mlp_predict(model, test_x)
print("预测类别：", pred)