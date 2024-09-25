from PIL import ImageGrab

snapshot = ImageGrab.grab()
snapshot.save(fp="neco.png")