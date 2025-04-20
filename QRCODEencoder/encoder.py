import qrcode

data = "This is my QrCode"
image = qrcode.make(data)
image.save("D:/QUARTER 3/QRCODEencoder/qrcode.png")

qr = qrcode.QRCode(version = 1, border= 5 , box_size= 10)
qr.add_data(data)
qr.add_data(data)
qr.make(fit=True)
image2 = qr.make_image(fill_color="white", back_color="black")
image2.save("D:/QUARTER 3/QRCODEencoder/qrcode2.png")