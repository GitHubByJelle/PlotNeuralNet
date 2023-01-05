import torchvision
import torch
import numpy as np

import torch.functional as F


class LeNet(torch.nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        # 1 input image channel (black & white), 6 output channels, 5x5 square convolution
        # kernel
        self.conv1 = torch.nn.Conv2d(2, 64, 3)
        self.conv2 = torch.nn.Conv2d(64, 64, 3)
        # an affine operation: y = Wx + b
        self.fc1 = torch.nn.Linear(64 * 2 * 2, 100)  # 6*6 from image dimension
        self.fc2 = torch.nn.Linear(100, 1)

    def forward(self, x):
        # Max pooling over a (2, 2) window
        print(x.shape)
        x = torch.relu(self.conv1(x))
        print(x.shape)
        # If the size is a square you can only specify a single number
        x = torch.relu(self.conv2(x))
        print(x.shape)
        x = torch.relu(self.conv2(x))
        print(x.shape)
        x = torch.relu(self.conv2(x))
        print(x.shape)
        x = x.view(-1, self.num_flat_features(x))
        print(x.shape)
        x = torch.relu(self.fc1(x))
        print(x.shape)
        x = torch.tanh(self.fc2(x))
        print(x.shape)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features

if __name__ == '__main__':
    net = LeNet()
    net = net.float()

    print(net)
    print(net.forward(torch.from_numpy(np.random.uniform(-1, 1, [1, 2, 10, 10])).float()))
