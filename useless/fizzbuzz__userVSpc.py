import time
def fizzbuzz(num):
    string = ""
    if num % 3 == 0:
        string += "Fizz"
    if num % 5 == 0:
        string += "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = str(num)
    return string


playing = True
while playing:
    number = 1
    for x in range(0, 100):
        print(fizzbuzz(number))
        number += 1
        user_guess = input("> ")
        right_guess = fizzbuzz(number)
        if user_guess.lower() == str(right_guess.lower()):
            pass
        else:
            print("wrong")
            break
        number += 1
    user_dec = input("Want to play again? ")
    if user_dec.lower() in ["y", "yes", "yeah", "ye"]:
        pass
    elif user_dec.lower() == "you go":
        for x in range(1, 101):
            print(fizzbuzz(x))
        s = input()
        exit()
    else:
        print("Thanks for playing then ❤")
        exit()
