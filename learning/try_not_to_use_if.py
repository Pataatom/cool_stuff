import os
import time
from functools import partial as prefill_args  # overkill, I use it to prefill the argument in the dict_of_subprograms

clear = lambda: os.system("cls")

class Subprograms():
    @classmethod
    def crossroad(cls, choice):
        dict_of_subprograms = {
            0: Subprograms.end_main,
            1: prefill_args(Subprograms.max_from_n_num, 2),  # argument 2 because we compare two numbers
            2: prefill_args(Subprograms.max_from_n_num, 3),
            3: Subprograms.switch_two_nums,
        }

        return dict_of_subprograms[choice]()  # return, so that ide don`t yell at me

    @staticmethod
    def end_main():
        ending_text = "Goodbye..."
        for index in range(len(ending_text)):
            print(ending_text[index], end="")
            time.sleep(0.15)

    @staticmethod
    def max_from_n_num(count_of_numbers):
        dict_of_nums = {
            0: "first",
            1: "second",
            2: "third",
            3: "fourth",
            4: "fifth",
            5: "sixth",
            6: "seventh",
        }
        list_of_numbers = []
        for num in range(count_of_numbers):
            x = int(input(f"{dict_of_nums[num]} num = "))
            list_of_numbers.append(x)
        print(max(list_of_numbers))  # using builtin function max because it is faster

    @staticmethod
    def switch_two_nums():
        list_of_numbers = []  # for such a dumb output too much work
        a = input("a = ")
        b = input("b = ")
        list_of_numbers.append(a); list_of_numbers.append(b)
        a = list_of_numbers[1]
        b = list_of_numbers[0]
        print(f"a = {a}\nb = {b}")

menu = [
    "___________________________",
    "0. end program",
    "1. max from 2 num",
    "2. max from 3 num",
    "3. switch two nums",
    "4. seconds to h:m:s format",
    "___________________________"
]

for line in range(len(menu)):
    print(menu[line])

# while loop for handling stoopid users
while True:
    user_choice = int(input("> "))
    if type(user_choice) is int and user_choice in range(0, 5):
        break

Subprograms.crossroad(user_choice)
