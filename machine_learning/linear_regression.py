import torch
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

torch.manual_seed(2)
X = torch.randn(100, 1) * 2
y = 3 * X + 2 + torch.randn(100, 1) * 0.5

#初始化参数
w = torch.randn(1, 1, requires_grad=True)
b = torch.randn(1, requires_grad=True)
# 替代 w 和 b 的手动初始化
# in_features=1, out_features=1 表示输入1维，输出1维
# model = nn.Linear(in_features=1, out_features=1)
# 使用 PyTorch 自带的优化器替代手动更新 (w -= lr * w.grad)
# optimizer = optim.SGD(model.parameters(), lr=0.01)

learning_rate = 0.01
epochs = 1000

#训练
for epoch in range(epochs):
    y_pred = X @ w + b
    # 替代 y_pred = X @ w + b
    # y_pred = model(X)
    loss = ((y_pred - y) ** 2).mean()
    loss.backward()     #反向传播，返回w，b的梯度

    with torch.no_grad():
        w -= learning_rate * w.grad
        b -= learning_rate * b.grad
    # 替代 with torch.no_grad(): w -= lr * w.grad ...
    # optimizer.step()  # 自动更新参数
    # optimizer.zero_grad()  # 替代 w.grad.zero_() 和 b.grad.zero_()

    w.grad.zero_()
    b.grad.zero_()

    if (epoch + 1) % 100 == 0:
        print(f"Epoch {epoch+1:4d} | Loss: {loss.item():.4f} | w: {w.item():.4f} | b: {b.item():.4f}")

print(f"\n真实参数: w=3, b=2")
print(f"训练后参数: w={w.item():.4f}, b={b.item():.4f}")

#可视化
plt.scatter(X.numpy(), y.numpy(), alpha=0.5, label='真实数据')
plt.plot(X.numpy(), (X @ w + b).detach().numpy(), color='red', linewidth=2, label='拟合直线')
plt.legend()
plt.title(f'Linear Regression: y = {w.item():.2f}x + {b.item():.2f}')
plt.show()