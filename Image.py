import random
from random import Random
from time import sleep

from PIL import Image as pil_image
from PIL import ImageDraw

def makeImage(res: tuple, matriz: tuple, S: int, color0: tuple, color1: tuple, color2: tuple, text: str) -> pil_image:

    X, Y = res  # Resolución de la imagen
    cols, rows = matriz

    # Crear imagen en blanco
    img = pil_image.new("RGBA", (X, Y), color2)
    draw = ImageDraw.Draw(img)

    fill = random.randint(3, (cols*rows) - len(text))
    lenTe = len(text)

    text = ("2"*fill) + text + ("2" * ((cols*rows) - fill - len(text)))

    lenTe2 = len(text)
    pixel = 0

    # Dibujar la cuadrícula
    for i in range(rows):
        for j in range(cols):
            x0 = j * S
            y0 = i * S
            x1 = x0 + S
            y1 = y0 + S

            if text[pixel] == "0":

                draw.rectangle([x0, y0, x1, y1], fill=color0)

            elif text[pixel] == "1":

                draw.rectangle([x0, y0, x1, y1], fill=color1)

            elif text[pixel] == "2":

                draw.rectangle([x0, y0, x1, y1], fill=color2)

            pixel +=1

    return img