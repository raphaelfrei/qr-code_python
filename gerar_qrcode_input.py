from logging import exception
import qrcode
from PIL import Image

from datetime import date

today = date.today()

texto = input("Insira um Texto...\n")

img = qrcode.make(texto)

output = ".\\qrcode_" + str(today) + ".png"

try:
    img.save(output)
except Exception as e:
    print(str(e))

print(img)
#img.show()