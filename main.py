import math
import random
from PIL import Image as pil_image
from PIL import ImageDraw
from ctypes.wintypes import PUINT
from time import sleep

import Image
import Pixels
import Text

resolution = (1080, 1080)
pixels = resolution[0] * resolution[1]
save_path = r"D:\datos\descargas\image.png"

text = Text.ascii_a_binario("Puto el que lo lea")

text_spaced = ""

for i in text:

    if i == "0" or i == "1":
        text_spaced += i

    else:

        text_spaced += ("2" * random.randint(1,5))

max_res = Pixels.getMaxRes(text_spaced, resolution)
# print(f"Max res: {max_res} - x:{max_res[0]*max_res[1]} y:{max_res[0]*max_res[2]} - {(resolution[0] * resolution[1])}")
# print(f"Sobrante - x{resolution[0]-max_res[0]*max_res[1]}, y{resolution[1]-max_res[0]*max_res[2]}")

img: pil_image = Image.makeImage(resolution, (max_res[1], max_res[2]), max_res[0], (0,0,0,255), (255,255,255,255), (202, 202, 202, 255), text_spaced)
img.save(save_path)