import pyfiglet
text = "some"
fonts = (pyfiglet.FigletFont.getFonts())
for x in fonts:
    print(f"↓↓↓  {x}  ↓↓↓")
    ascii_art = pyfiglet.figlet_format(text, font= x)
    print(ascii_art)
exit = input()
