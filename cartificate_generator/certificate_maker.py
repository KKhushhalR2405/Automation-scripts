from matplotlib import pyplot as plt

import pandas as pd

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


# --------------------------#

file = pd.read_csv("participants.csv", sep=',')

img = Image.open("template.png")

# ---------------------------#

for j in range(len(file.columns)):
    i = img.copy()
    i = i.resize((3000, 2121))

    img1 = ImageDraw.Draw(i)

    font0 = ImageFont.truetype(r'fonts/Piazzolla/Piazzolla-VariableFont_opsz,wght.ttf', 80)

    font1 = ImageFont.truetype(r'fonts/Piazzolla/Piazzolla-ExtraBoldItalic-opsz=8.ttf', 130)

    font2 = ImageFont.truetype(r'fonts/Piazzolla/Piazzolla-VariableFont_opsz,wght.ttf', 70)

    font3 = ImageFont.truetype(r'fonts/Piazzolla/Piazzolla-ExtraBoldItalic-opsz=8.ttf', 60)

    text0 = "THIS   IS   PRESENTED   TO  \n"
    text1 = file.name[j] + "\n"
    text2 = "for    taking    part    in    Hacktoberfest    and    \ncontribution    in    #" + str(file.pr[j]) + "    at    " + str(file.repo[j]) + "  .\n"
    text3 = file.maintainer[j]
    img1.text((1017, 1229), text0, (0, 0, 0), font=font0)
    img1.text((1017, 1337), text1, (51, 253, 153), font=font1)
    img1.text((1017, 1557), text2, (0, 0, 0), font=font2)
    img1.text((413, 1835), text3, (255, 51, 153), font=font3)


    path = r"output/certificate-" + str(file.name[j]) + ".png"  # Output path

    plt.figure()
    plt.imshow(i)

    i.save(path)
    print("\n")

# ----------------------------#
