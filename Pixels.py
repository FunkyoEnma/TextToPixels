import math
from time import sleep


def getMaxRes(text: str, resolution: tuple):

    smax = min(resolution)
    smin = math.sqrt((resolution[0] * resolution[1]) / len(text))

    print(len(text), "-", resolution[0] * resolution[1], "-", smax, "-", smin, "-",
          smin * smin * len(text))

    lant = 0
    lact = smax
    x = 0
    reducing = False

    while True:

        # iteramos para encontrar el número más optimo

        cxy = math.floor(resolution[0] / lact) * math.floor(resolution[1] / lact)

        if reducing:

            if cxy > len(text):


                #print(f"ENTERING - Cx:{resolution[0] / lact} - Cy:{resolution[1] / lact} - "
                #      f"Res:{cxy}"
                #      f" - Req:{len(text)} - Lact:{lact}")

                if cxy > len(text):
                    return lact, math.floor(resolution[0] / lact), math.floor(resolution[1] / lact)

                tmp = math.floor((lant - lact) / 2) + lact

                cx = math.floor(resolution[0] / tmp)
                cy = math.floor(resolution[1] / tmp)
                cxy = cx * cy

                if cxy > len(text):
                    return lact, math.floor(resolution[0] / lact), math.floor(resolution[1] / lact)

                lact = tmp

                sleep(1)

            else:

                tmp = math.floor((lant - lact) / 2)

                cx = math.floor(resolution[0] / tmp)
                cy = math.floor(resolution[1] / tmp)
                cxy = cx * cy

                #print(f"ENTERING2 - Cx:{resolution[0] / lact} - Cy:{resolution[1] / lact} - "
                #      f"Res:{cxy}"
                #      f" - Req:{len(text)} - Lact:{lact}")

                lact = tmp

                sleep(1)


        else:
            # Guardamos valor anterior para ajuste maximo
            lant = lact

            # intentamos con la mitad del valor máximo
            tmp = math.floor(lact / 2)

            cx = math.floor(resolution[0] / tmp)
            cy = math.floor(resolution[1] / tmp)
            cxy = cx * cy

            #print(
            #    f"Cx:{resolution[0] / tmp} - Cy:{resolution[1] / tmp} - Res:{cxy} - Req:{len(text)} - Lact:{tmp}")

            if cxy > len(text):
                reducing = True
                orientation = "Right"

            lact = tmp
            sleep(1)

        x += 1