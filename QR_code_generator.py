import qrcode as qr
a=str(input("link:"))
img=qr.make(a)
img.save("qr_code.png")
print("your QR is generated !")
