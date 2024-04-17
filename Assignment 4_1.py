import qrcode

name = input ("enter your name: ")
number = input("enter your phone number: ")
a = name + number
x = qrcode.make(a)
x.save("QRcode.png")
