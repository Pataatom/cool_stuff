from PIL import Image

ascii_characters_by_surface_65 = '`^"' + r",:;Il!i~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_characters_by_surface_10 = " .:-=+*#%@"
if int(input("65 or 10> ")) == 10:
    ascii_characters_by_surface = ascii_characters_by_surface_10

    # stupid reversing string

    ascii_list = list(ascii_characters_by_surface)
    ascii_list.reverse()
    ascii_characters_by_surface = ""
    for char in ascii_list:
        ascii_characters_by_surface += char
    # stupid reversing string

else:
    ascii_characters_by_surface = ascii_characters_by_surface_65
'''    # stupid reversing string
    ascii_list = list(ascii_characters_by_surface)
    ascii_list.reverse()
    ascii_characters_by_surface = ""
    for char in ascii_list:
        ascii_characters_by_surface += char'''
    # stupid reversing string


def pixel_to_ascii(pixel):
    '''
    pixel_brightness = pixel
    max_brightness = 256
    brightness_weight = len(ascii_characters_by_surface) / max_brightness
    index = int(pixel_brightness * brightness_weight)
    return ascii_characters_by_surface[index]
    '''


#  ____if rgb than use this____
    if isinstance(pixel, int):
        # Handle grayscale images where the pixel is an integer
        pixel_brightness = pixel
        max_brightness = 255
    else:
        # Extract color channels from the pixel tuple
        (R, G, B, A) = pixel
        if A == 0:
            pixel_brightness = 0
        else:
            pixel_brightness = 0.299 * R + 0.587 * G + 0.114 * B
        max_brightness = 0.299 * 255 + 0.587 * 255 + 0.114 * 255
    brightness_weight = len(ascii_characters_by_surface) / max_brightness
    index = int(pixel_brightness * brightness_weight)
    print(pixel)
    print(pixel_brightness)
    print(index)
    if index == 0:
        return ascii_characters_by_surface[index]
    elif index > 9:
        pass
    else:
        index -= 1
        return ascii_characters_by_surface[index]
'''
if pixel_brightness == 0:
    return " "
else:
    index -= 1
    return ascii_characters_by_surface[index]
'''


def main(pic):
    image = Image.open(pic)
    (width, height) = image.size
    new_height = int(height/2.5)
    image = image.resize((width, new_height))
    ascii_art = []
    for y in range(new_height):
        line = ""
        for x in range(width):
            px = image.getpixel((x, y))
            line += pixel_to_ascii(px)
        ascii_art.append(line)
    saving_ascii_art(ascii_art)  # Call the saving_ascii_art function to save the ASCII art


def saving_ascii_art(ascii_art):
    with open("ascii_image.txt", "w") as f:
        for line in ascii_art:
            f.write(line)
            f.write("\n")


if __name__ == '__main__':
    main(r"C:\Users\pataa\Downloads\ghost.png")
