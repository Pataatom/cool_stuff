from PIL import Image

ascii_characters_by_surface_10 = " .:-=+*#%@"
ascii_characters_by_surface = ascii_characters_by_surface_10

# stupid reversing string
ascii_list = list(ascii_characters_by_surface)
ascii_list.reverse()
ascii_characters_by_surface = ""
for char in ascii_list:
    ascii_characters_by_surface += char
# stupid reversing string


def pixel_to_ascii(pixel, extension):
    if
    print(pixel)
    if isinstance(pixel, int):  # Handle grayscale images where the pixel is an integer
        pixel_brightness = pixel
        max_brightness = 255
    else:  # Extract color channels from the pixel tuple
        (R, G, B, A) = pixel
        pixel_brightness = 0.299 * R + 0.587 * G + 0.114 * B
        max_brightness = 0.299 * 255 + 0.587 * 255 + 0.114 * 255
        brightness_weight = len(ascii_characters_by_surface) / max_brightness
        index = int(pixel_brightness * brightness_weight)
        if index == 0 and A > 0:  # is it black???
            pass
        else:
            index -= 1
        return ascii_characters_by_surface[index]
        # sadly, with this logic, the true white (255, 255, 255, 255) will never be " " (blank)
        # I know there is some clear solution to this, but I am just too dumb


def main(pic):
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
    for y in range(new_height):
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


if __name__ == '__main__':
    main(r"C:\Users\pataa\Downloads\troll.jpg")
