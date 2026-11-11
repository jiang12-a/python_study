import torch
import torch.nn as nn
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

torch.manual_seed(30)

x = torch.randn(1024,2)
t = torch.sin(x[:,0:1]) + torch.cos(x[:,1:2])

#划分测试集与训练集
idx = torch.randperm(1024)
x_train , t_train = x[idx[:580]] , t[idx[:580]]
x_test , t_test = x[idx[580:]] , t[idx[580:]]
# x = torch.tensor([[1.]])
# t = torch.tensor([[0.]])

def build_mlp(input_dim , hidden_dim ,output_dim):
    layers = []
    prev = input_dim
    for i in hidden_dim:
        layers.append(nn.Linear(prev , i))
        layers.append(nn.ReLU())
        layers.append(nn.Dropout(0.01))
        prev = i
    layers.append(nn.Linear(prev , output_dim))
    return nn.Sequential(*layers)

model = build_mlp(input_dim = 2 ,hidden_dim = [64,64] , output_dim = 1)

# model = torch.nn.Sequential(
#     nn.Linear(1, 1, False),
#     nn.ReLU(),
#     nn.Linear(1, 1, False),
#     nn.ReLU(),
#     nn.Linear(1, 1, False),
# )

# for m in model.modules():
#     if isinstance(m, nn.Linear):
#         nn.init.kaiming_normal_(m.weight)
#         if m.bias is not None:
#             nn.init.zeros_(m.bias)

# with torch.no_grad():
#     model[0].weight.fill_(2.)
#     model[2].weight.fill_(3.)
#     model[4].weight.fill_(-1.)

criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)

epoch_list = []
train_loss_list = []
test_loss_list = []
w1_list = []
w2_list = []
w3_list = []

for epoch in range(1000):
    model.train()
    optimizer.zero_grad()
    # z1 = model[0](x)
    # a1 = model[1](z1)
    # z2 = model[2](a1)
    # a2 = model[3](z2)
    # output = model[4](a2)
    output = model(x_train)
    loss = criterion(output, t_train)
    loss.backward()
    # if epoch % 10 == 0:
    #     print(f"epoch: {epoch + 1}")
    #     print(f"z1: {z1} -> a1: {a1} -> z2: {z2} -> a2: {a2} -> output: {output} ")
    optimizer.step()

    model.eval()
    with torch.no_grad():
        test_output = model(x_test)
        test_loss = criterion(test_output , t_test)

    epoch_list.append(epoch + 1)
    train_loss_list.append(loss.item())
    test_loss_list.append(test_loss.item())

    # w1_list.append(model[0].weight.item())
    # w2_list.append(model[2].weight.item())
    # w3_list.append(model[4].weight.item())

    if epoch % 50 == 0:
        print(f"epoch:{epoch + 1} , train loss:{loss.item()} , test loss:{test_loss.item()}")
        # print(f"当前的w1 = {model[0].weight.data}")
        # print(f"当前的w2 = {model[2].weight.data}")
        # print(f"当前的w3 = {model[4].weight.data}")

fig, ax1,  = plt.subplots(1, 1, figsize=(8,6))

#loss曲线
ax1.plot(epoch_list, train_loss_list, color = "red" , label = "train loss")
ax1.plot(epoch_list, test_loss_list, color = "blue" , label = "test loss")
ax1.set_title("LOSS 随训练轮次变化")
ax1.set_xlabel("epoch")
ax1.set_ylabel("loss")
ax1.legend()
ax1.grid(alpha = 0.2)

plt.tight_layout()
plt.show()