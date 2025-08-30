import qrcode
img = qrcode.make('http://localhost:8000')
img.save("menu_qr.png")
