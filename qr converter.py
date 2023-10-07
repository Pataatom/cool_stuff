import qrcode
promt = input("What to convert: ")
img = qrcode.make(promt)
name = str(input("Name of the file: "))
img.save(name + ".png")