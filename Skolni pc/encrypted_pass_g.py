import string
import random
import time
password = ""
list_of_char = string.ascii_letters + string.digits + string.punctuation
list_of_char = list(list_of_char)
while True:
    try:
        digits_in_password = int(input("> "))
        break
    except:
        pass
for x in range(digits_in_password):
    password += random.choice(list_of_char)
time.sleep(1)
print(password)
time.sleep(1)
choice = input("do you want to save password? ")
if choice.lower() in ("yes", "y"):
    usable_list = string.ascii_letters + string.punctuation + string.digits + " "
    usable_list = list(usable_list)
    key = ['(', 'q', '{', '>', ',', 'm', '9', 'a', '.', '3', '}', 'o', '_', ']', 'v', 'Y', '/', '!', 'M', 't', '6', '$', 'c', 'T', '|', 'f', '"', '\\', 'V', 'g', '2', 'r', ';', 'W', 'G', ')', 'i', 'K', '[', '7', 's', '8', 'S', '1', 'Z', 'y', 'C', '*', 'I', 'e', '#', 'n', 'P', '~', '<', '^', 'J', 'D', '?', 'O', '5', 'h', 'z', '-', 'd', 'j', 'B', 'R', 'X', 'H', "'", 'A', ':', '`', 'Q', 'u', '&', 'U', 'F', '@', 'b', 'p', '=', 'E', '%', '+', 'L', 'k', 'l', 'N', '4', 'x', '0', 'w']
    output = ""
    decisi = "en"
    if decisi.lower() == "en":
        mess = password
        for letter in mess:
            index = usable_list.index(letter)
            output += key[index]
    elif decisi.lower() == "de":
        mess_de = input("text to decrypt> ")
        for letter in mess_de:
            index = key.index(letter)
            output += usable_list[index]
    print(output)
    for_wha = input("For what do you wan't to use password? ")
    with open("not_pass.txt", "a") as f:
        f.write(f"{for_wha}:  {output}\n")
    print("note that password is encrypted, for decryption use end000")
