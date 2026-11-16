import torch.nn as nn
import torch.nn.functional as F
#前置层
class PreLayer(nn.Module):
    def __init__(self):
        super(PreLayer, self).__init__()
        self.pre = nn.Sequential(
            nn.Conv2d(3, 64, 7, 2, 3, bias = False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace = True),
            nn.MaxPool2d(3, 2, 1),
        )

    def forward(self, x):
        return self.pre(x)
#残差块
class ResidualBlock(nn.Module):
    def __init__(self , in_channel , out_channel ,stride = 1 , shortcut = None):
        super(ResidualBlock,self).__init__()
        self.left = nn.Sequential(
            nn.Conv2d(in_channel , out_channel , 3 , stride , 1 , bias = False),
            nn.BatchNorm2d(out_channel),
            nn.ReLU(inplace = True),
            nn.Conv2d(out_channel , out_channel , 3 , 1 , 1 ,  bias = False),
            nn.BatchNorm2d(out_channel),
        )
        self.right = shortcut

    def forward(self , x):
        res = x if self.right is None else self.right(x)
        x = res  + self.left(x)
        x = F.relu(x)
        return x

class MakeLayers(nn.Module):
    def __init__(self , in_channel, out_channel, block_num, stride, is_shortcut = True):
        super(MakeLayers,self).__init__()
        #残差连接
        if is_shortcut:
            shortcut = nn.Sequential(
                nn.Conv2d(in_channel, out_channel, 1, stride = stride, bias = False),
                nn.BatchNorm2d(out_channel)
            )
        else:
            shortcut = None
        layers = []
        layers.append(ResidualBlock(in_channel , out_channel , stride , shortcut))
        for _ in range(block_num - 1):
            layers.append(ResidualBlock(out_channel , out_channel , stride = 1 , shortcut = None))
        self.layers =  nn.Sequential(*layers)

    def forward(self, x):
        return self.layers(x)
#ResNet
class ResNet(nn.Module):
    def __init__(self , num_classes = 1000):
        super(ResNet,self).__init__()
        #前置层
        self.pre = PreLayer()
        #中间块
        self.layer1 = MakeLayers(64 , 64 ,3 , 1 , False)
        self.layer2 = MakeLayers(64 , 128 , 4 , 2 , True)
        self.layer3 = MakeLayers(128 , 256 , 6 , 2 , True)
        self.layer4 = MakeLayers(256 , 512 ,3 , 2 , True)
        #分类
        self.classifier = nn.Linear(512 , num_classes)

    def forward(self, x):
        x = self.pre(x)
        x= self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = F.avg_pool2d(x , 7)
        x = x.view(x.size(0) , -1)
        x = self.classifier(x)
        return x


