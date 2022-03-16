from PIL import Image
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from efficientnet_pytorch import EfficientNet


classes = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'non-recyclable']
cn_classes = ['纸板','玻璃','金属','可回收纸','塑料','不可回收垃圾']

class EffNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.network = EfficientNet.from_name('efficientnet-b4')
        in_features = self.network._fc.in_features
        self.network._fc = nn.Linear(in_features, len(classes))

    def forward(self, xb):
        return F.relu(self.network(xb))


model = EffNet()
test_transforms = transforms.Compose([transforms.Resize(256),
                                      transforms.GaussianBlur(9),
                                      transforms.ToTensor(),
                                      ])


def load_model():
    model.load_state_dict(torch.load('./model/weight2.pth',map_location='cpu'))
    model.eval()


def predict_img(image_path):
    image = Image.open(image_path)
    img_tensor = test_transforms(image)
    img_tensor = img_tensor.unsqueeze(0)
    output = model(img_tensor)
    prob, preds = torch.max(output, dim=1)
    print(prob)
    print(preds)
    return cn_classes[preds[0].item()]


load_model()
