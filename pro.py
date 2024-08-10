import qrcode
data="https://satwik794.github.io/index/"
qr=qrcode.make(data)
qr.save("github.png")
qr.show()
