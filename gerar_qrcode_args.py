import qrcode
import sys

from datetime import date

today = date.today()

texto = sys.argv[1]

img = qrcode.make(texto)

output = "qrcode_" + str(today) + ".png"

img.save(output)

img.show()