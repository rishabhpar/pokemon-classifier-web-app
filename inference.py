import json
import io
import torch
from PIL import Image
import torchvision.transforms as transforms

cat_to_name = {1: 'Bulbasaur', 2: 'Charmader', 3: 'Pikachu', 4: 'Squirtle'}

model = torch.load('model.pth', map_location='cpu')
model.eval()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

test_transforms = transforms.Compose([transforms.Resize(224),
                                      transforms.ToTensor(),
                                     ])


def get_pokemon_name(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')

    image_tensor = test_transforms(image).float()
    image_tensor = image_tensor.unsqueeze_(0)

    input = image_tensor.to(device)
    output = model(input)

    index = output.data.cpu().numpy().argmax()
    print(index)
    pokemon_name = cat_to_name[index]
    return pokemon_name
