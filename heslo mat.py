import random
import string
import time


def main(length, special_char):
    password = ""
    if special_char:
        possibilities = ["spec_char", "number", "char_lower", "char_upper"]
    else:
        possibilities = ["number", "char_lower", "char_upper"]
    while length != 0:
        char_in_pass = random.choice(possibilities)
        if char_in_pass == "number":
            password += str(random.randint(0, 9))
        elif char_in_pass == "char_upper":
            password += random.choice(string.ascii_uppercase)
        elif char_in_pass == "char_lower":
            password += random.choice(string.ascii_lowercase)
        elif char_in_pass == "spec_char":
            password += random.choice(string.punctuation)
        length -= 1
    return password


def download(password, pilot_licenc_what_for):
    with open("Kuře na paprice.txt", "a") as f:
        f.write(f"{pilot_licenc_what_for}: {password} \n")


def interface():
    length = ""
    choice = ""
    store = ""
    while type(length) != int:
        length = input("Počet znaků v hesle, které má být vytvořeno (doporučeno min 8) > ")
        try:
            length = int(length)
        except:
            pass
    while choice.lower() not in ["ano", "ne", "a", "n", "yes", "y", "no"]:
        choice = input("chcete speciální znaky? > ")
    if choice.lower() in ("ano", "a"):
        spec_char = True
    else:
        spec_char = False
    password = main(length, spec_char)
    print(f"Vaše heslo je: {password}")
    time.sleep(2)
    while store.lower() not in ("ano", "ne", "a", "n", "y", "n"):
        store = input("Chcete uložit heslo? ")
        if store.lower() in ("y", "a", "ano"):
            what_for = input("Na co hodláte heslo použít:  ")
            download(password, what_for)
        elif store.lower() in ("n", "ne"):
            print("MADE BY pataatom")
            exit()
        else:
            print("Bad input")
            pass


interface()
