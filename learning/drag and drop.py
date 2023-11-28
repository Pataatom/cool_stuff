import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
import os
from PIL import Image
from tqdm import tqdm


ascii_characters_by_surface_10 = " .:-=+*#%@"
ascii_characters_by_surface_65 = '`^"' + r",:;Il!i~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_characters_by_surface = ascii_characters_by_surface_10

# stupid reversing string
ascii_list = list(ascii_characters_by_surface)
ascii_list.reverse()
ascii_characters_by_surface = ""
for char in ascii_list:
    ascii_characters_by_surface += char
# stupid reversing string


def pixel_to_ascii(pixel, extension):
    if extension == ".png":
        if isinstance(pixel, int):  # Handle grayscale images where the pixel is an integer(never needed this)
            pixel_brightness = pixel
            max_brightness = 255
        else:  # Extract color channels from the pixel tuple
            try:
                (R, G, B, A) = pixel
            except:
                (R, G, B) = pixel
                A = 1
            pixel_brightness = 0.299 * R + 0.587 * G + 0.114 * B
            max_brightness = 0.299 * 255 + 0.587 * 255 + 0.114 * 255
            brightness_weight = len(ascii_characters_by_surface) / max_brightness
            index = int(pixel_brightness * brightness_weight)
            if index == 0 and A > 0:  # is it black???
                pass
            else:
                index -= 1
            return ascii_characters_by_surface[index]
    elif extension == ".jpg":
        if isinstance(pixel, int):  # Handle grayscale images where the pixel is an integer(never needed this)
            pixel_brightness = pixel
            max_brightness = 255
        else:  # Extract color channels from the pixel tuple
            (R, G, B) = pixel
            pixel_brightness = 0.299 * R + 0.587 * G + 0.114 * B
            max_brightness = 0.299 * 255 + 0.587 * 255 + 0.114 * 255
            brightness_weight = len(ascii_characters_by_surface) / max_brightness
            index = int(pixel_brightness * brightness_weight)
            if index == 0:  # is it black???
                pass
            else:
                index -= 1
            return ascii_characters_by_surface[index]
            # sadly, with this logic, the true white (255, 255, 255, 255) will never be " " (blank)
            # I know there is some clear solution to this, but I am just too dumb


def working_with_picture(pic):
    if ".jpg" in pic:
        extension = ".jpg"
    elif ".png" in pic:
        extension = ".png"
    else:
        print("Bad file extension, need .jpg or .png")
        input()
        exit()
    image = Image.open(pic)
    (width, height) = image.size
    new_height = int(height*0.3676470588235294)
    image = image.resize((width, new_height))
    ascii_art = []
    for y in tqdm(range(new_height)):
        line = ""
        for x in range(width):
            px = image.getpixel((x, y))
            line += pixel_to_ascii(px, extension)
        ascii_art.append(line)
    saving_ascii_art(ascii_art)  # Call the saving_ascii_art function to save the ASCII art


def saving_ascii_art(ascii_art):
    with open("ascii_image.txt", "w") as f:
        for line in ascii_art:
            f.write(line)
            f.write("\n")

def on_drop(event):
    file_path = event.data
    file_name = os.path.basename(file_path)
    working_with_picture(str(file_path))


def main():
    root = TkinterDnD.Tk()
    label = tk.Label(root, text="Drag and drop files onto this label")
    label.pack(padx=10, pady=10)
    label.drop_target_register(DND_FILES)
    label.dnd_bind('<<Drop>>', on_drop)
    root.mainloop()

if __name__ == '__main__':
    main()