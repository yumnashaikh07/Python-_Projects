from pyzbar.pyzbar import decode
from PIL import Image


image = Image.open("D:/QUARTER 3/QRCODEencoder/qrcode.png")
result = decode(image)
print(result)
