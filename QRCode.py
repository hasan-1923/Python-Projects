import qrcode 


code =qrcode.make("https://www.python.org/")
code.save("qrcode1.png")