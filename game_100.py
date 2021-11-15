# Easy python game
#Game is called 100
#Objective of the game is 2 people to pick numbers from 1 to 10 and on each turn they add the sum of the values up
#The perosn who losses is the person who cannot use the last turn to reach 100

from random import Random, randint
import tkinter as tk

def reverse_user_pick(choice):
    a = choice
    c = a.lower()
    if c == "head" or c == "heads":
        return "Coin Result:: Tails"
    elif c == "tail" or c == "tails":
        return "Coin Result:: Heads"
    else:
        return "This value you entered in Valid \n enter either Heads or Tails"

def user_pick():
    p = input("To decide who begins first enter 'heads' or 'tails':....")
    return str(p)

pick = user_pick()

print(reverse_user_pick(pick))

#The basic algorithem that will let the AI always win


window = tk.Tk()

def check_length(x):

    return (11 - int(x))


def game_fun():
    counter = 0
    counter += 1
    print("AI Number:  1")
    
    #For the algorithm to work the ai must have the first pick of 1
    while counter < 100:
           

        user_input_first = input("Choose a number: ")
        user_input = int(user_input_first)
        if int(user_input) > 10 or int(user_input) < 1:
            print("Sorry incorect number")
            break
        assert type(user_input) == int, "Value is not an Integer"
            #ensure that the user choice is within bound

        print("User Pick:" + str(user_input))
        counter += int(user_input)
        print(counter)
        counter += check_length(user_input)
        #Ai will use the users input to get the correct pick

        ai_pick = check_length(user_input)
        print("Ai Number: ", ai_pick)
        print((counter))

game_fun()



#List of possible end game statements can easily be added
statements = ["HAHA YOU LOST", "YOU ARE TRASH DELETE YOURSELF", "UNLUCKY BOI", "FIND ANOTHER GAME", "CLOSE GAME", "BETTER LUCK NEXT TIME", "STOP EMBARRASING YOURSELF"]

random_number = randint(0, len(statements) - 1)

#this funtion will randomly pick a statment to display
def show_end(ran, stat):
    return stat[ran]


text_to_show = (show_end(random_number, statements))

greeting = tk.Label(text=text_to_show)

greeting.pack()

window.mainloop()
