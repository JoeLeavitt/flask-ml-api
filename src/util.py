from PIL import Image
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 86)
        self.fc2 = nn.Linear(86, 86)
        self.fc3 = nn.Linear(86, 86)
        self.fc4 = nn.Linear(86, 10)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return F.log_softmax(x, dim=1)

def prepare_image(img):
    # open as grayscale image
    img = Image.open(img).convert("L")

    # resize to 28X28 pixels like those in MNIST test set
    img = img.resize((28, 28))

    # convert to tensor
    to_tensor = transforms.ToTensor()
    tensor = to_tensor(img)

    # flatten tensor
    flat_tensor = tensor.view(-1, 784)

    return flat_tensor

