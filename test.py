import os 
from PIL import Image

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(ROOT_DIR, 'images')

image = Image.open(os.path.join(IMAGE_DIR, 'mic.png'))
w, h = image.size
print(w/4, h/4)
