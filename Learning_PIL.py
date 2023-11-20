from PIL import Image, ImageEnhance

img = Image.open(r"C:\Users\pataa\OneDrive\Obrázky\MONKEY.png")

img = img.convert("L")

img.show()