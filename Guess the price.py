#This program will choose randomly a number between 1 and 100.
#You have 5 guesses.
#Good luck!!!!

import random

# random price choice
price = random.randint(1, 100)

trys = 0

print("You have 5 chances.")

while True:
    nombre = int(input("Choose a number between 1 and 100 : "))
    # add a try everytime you guess
    trys += 1
    #stop the game if too much trys
    if trys == 5 :
        print("You lost, too much trys.")
        print("The guess was", price)
        break
    #says if the price is higher or lower
    if nombre < price :
        print("Price is higher.")
        print("You did", trys, "/5 trys")
    if nombre > price :
        print("Price is lower.")
        print("You did", trys, "/5 trys")
    #congrats you if you win
    if nombre == price :
        print("You won. The price was", price)
        print("You did it in", trys, " trys")
        break