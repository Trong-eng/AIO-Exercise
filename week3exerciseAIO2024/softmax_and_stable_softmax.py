import torch
import torch.nn as nn
class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        x_exp = torch.exp(x)
        sum_exp = x_exp.sum(0, keepdims = True)#calculate the sum during the dim = 0 and stay at that dim
        return x_exp / sum_exp
mysoftmax = MySoftmax()
data = torch.Tensor(([1 , 2 , 300000000]))
output = mysoftmax(data)
print(output)
class StableMySoftmax(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        c = torch.max(x, dim =0)#find the max during the dim = 0
        x_exp = torch.exp(x - c.values)
        sum_exp = x_exp.sum(0, keepdims = True)
        return x_exp / sum_exp
stable_softmax = StableMySoftmax()
data1 = torch.Tensor([1,2,3])
output1 = stable_softmax(data1)
print(output1)