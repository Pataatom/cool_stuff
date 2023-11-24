import string
import random
usable_list = string.ascii_letters + string.punctuation + string.digits + " "
usable_list = list(usable_list)
#key = usable_list.copy()
#andom.shuffle(key)

key = ['(', 'q', '{', '>', ',', 'm', '9', 'a', '.', '3', '}', 'o', '_', ']', 'v', 'Y', '/', '!', 'M', 't', '6', '$', 'c', 'T', '|', 'f', '"', '\\', 'V', 'g', '2', 'r', ';', 'W', 'G', ')', 'i', 'K', '[', '7', 's', '8', 'S', '1', 'Z', 'y', 'C', '*', 'I', 'e', '#', 'n', 'P', '~', '<', '^', 'J', 'D', '?', 'O', '5', 'h', 'z', '-', 'd', 'j', 'B', 'R', 'X', 'H', "'", 'A', ':', '`', ' ', 'Q', 'u', '&', 'U', 'F', '@', 'b', 'p', '=', 'E', '%', '+', 'L', 'k', 'l', 'N', '4', 'x', '0', 'w']
go = True
while go:
    output = ""
    decisi = input("Do you want to (en)crypt or (de)crypt> ")
    if decisi.lower() == "en":
        mess = input("text to encrypt> ")
        for letter in mess:
            index = usable_list.index(letter)
            output += key[index]
    elif decisi.lower() == "de":
        mess_de = input("text to decrypt> ")
        for letter in mess_de:
            index = key.index(letter)
            output += usable_list[index]
    print(output)
    
