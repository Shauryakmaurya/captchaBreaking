import torch
from torch import nn
from torch.nn import functional as F


class CaptchaClassifier(nn.Module):
    def __init__(self, num_classes=100):
        super(CaptchaClassifier, self).__init__()
        self.conv_1 = nn.Conv2d(3, 128, kernel_size=(3, 6), padding=(1, 1))
        self.pool_1 = nn.MaxPool2d(kernel_size=(2, 2))
        self.conv_2 = nn.Conv2d(128, 64, kernel_size=(3, 6), padding=(1, 1))
        self.pool_2 = nn.MaxPool2d(kernel_size=(2, 2))
        self.linear_1 = nn.Linear(1152, 64)
        self.drop_1 = nn.Dropout(0.2)
        self.lstm = nn.GRU(64, 32, bidirectional=True, num_layers=2, dropout=0.25, batch_first=True)
        self.output = nn.Linear(64, num_classes)

    def forward(self, images):
        bs, _, _, _ = images.size()
        x = F.relu(self.conv_1(images))
        x = self.pool_1(x)
        x = F.relu(self.conv_2(x))
        x = self.pool_2(x)
        x = x.permute(0, 3, 1, 2)
        x = x.view(bs, x.size(1), -1)
        x = F.relu(self.linear_1(x))
        x = self.drop_1(x)
        x, _ = self.lstm(x)
        x = x[:, -1, :]  # Take last time step output
        x = self.output(x)
        return x


if __name__ == "__main__":
    model = CaptchaClassifier(num_classes=100)
    img = torch.rand((1, 3, 50, 200))
    output = model(img)
    print(output.shape)  # Should be (1, 100)
