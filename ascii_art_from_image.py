from PIL import Image

ascii_characters_by_surface_65 = '`^"' + r",:;Il!i~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_characters_by_surface_10 = ".:-=+*x#%@"



def pixel_to_ascii(pixel):
    if isinstance(pixel, int):
        # Handle grayscale images where the pixel is an integer
        pixel_brightness = pixel
    else:
        # Extract color channels from the pixel tuple
        (R, G, B) = pixel[:3]
        pixel_brightness = 0.299 * R + 0.587 * G + 0.114 * B
    max_brightness = 255 * 3
    brightness_weight = len(ascii_characters_by_surface_65) / max_brightness
    index = int(pixel_brightness * brightness_weight)
    if index == 0:
        return " "
    else:
        index -= 1
        return ascii_characters_by_surface_65[index]


def main(pic):
    image = Image.open(pic)
    (width, height) = image.size
    ascii_art = []
    for y in range(height):
        line = ""
        for x in range(width):
            px = image.getpixel((x, y))
            line += pixel_to_ascii(px)
        ascii_art.append(line)
    # saving_ascii_art(ascii_art)  # Call the saving_ascii_art function to save the ASCII art


def saving_ascii_art(ascii_art):
    with open("ascii_image.txt", "w") as f:
        for line in ascii_art:
            f.write(line)
            f.write("\n")


if __name__ == '__main__':
    main("power-on.png")
