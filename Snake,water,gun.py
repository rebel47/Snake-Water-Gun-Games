# # Snake Water Gun

import random
import shutil
from simple_colors import *
columns = shutil.get_terminal_size().columns
print(magenta("***Welcome to Snake Water Gun Game***".center(columns)))
print(red("Developed by A2Z Developers".center(columns)))
print(blue("!!!You got 10 chances only!!!".center(columns)))
print("\n")
def action():
    human_point = 0
    comp_point = 0
    n = 1
    while(n<=10):
        arr = ["snake", "water", "gun"]
        take = random.choice(arr)
        a = input(cyan("snake/water/gun: "))
        if a=='snake':
            if take=='snake':
                print("Draw")
                print("Computer choose :",take)
                print("Both Get's 0 point!!")
                print("Your Point: ", human_point)
                print("Comp Point: ", comp_point)
                print(10-n,"chances left!!!")
                print("\n \n")
            elif take=='water':
                print("You Won")
                print("Computer choose :",take)
                human_point = human_point + 1
                print("Your Point: ",human_point)
                print("Comp Point: ",comp_point)
                print(10-n,"chances left!!!")
                print("\n \n")

            elif take=='gun':
                print("You Loose")
                print("Computer choose :",take)
                comp_point = comp_point + 1
                print("Your Point: ", human_point)
                print("Comp Point: ", comp_point)
                print(10-n,"chances left!!!")
                print("\n \n")

        elif a=='water':
            if take=='snake':
                print("You Loose")
                print("Computer choose :",take)
                comp_point = comp_point + 1
                print("Your Point: ", human_point)
                print("Comp Point: ", comp_point)
                print(10-n,"chances left!!!")
                print("\n \n")

            elif take=='water':
                print("Draw")
                print("Computer choose :",take)
                print("Both Get's 0 point!!")
                print("Your Point: ", human_point)
                print("Comp Point: ", comp_point)
                print(10-n,"chances left!!!")

                print("\n \n")
            elif take=='gun':
                print("You Won")
                print("Computer choose :",take)
                human_point = human_point + 1
                print("Your Point: ", human_point)
                print("Comp Point: ", comp_point)
                print(10-n,"chances left!!!")

                print("\n \n")

        elif a=='gun':
            if take=='snake':
                print("You Won")
                print("Computer choose :",take)
                human_point = human_point + 1
                print("Your Point: ", human_point)
                print("Comp Point: ", comp_point)
                print(10-n,"chances left!!!")
                print("\n \n")

            elif take=='water':
                print("You Loose")
                print("Computer choose :",take)
                comp_point = comp_point + 1
                print("Your Point: ", human_point)
                print("Comp Point: ", comp_point)
                print(10-n,"chances left!!!")
                print("\n \n")

            elif take=='gun':
                print("Draw")
                print("Computer choose :",take)
                print("Both Get's 0 point!!")
                print("Your Point: ", human_point)
                print("Comp Point: ", comp_point)
                print(10-n,"chances left!!!")
                print("\n \n")
        n = n+1



    if human_point > comp_point:
        print(green("****!!!YOU WON!!!****".center(columns)))
        print("\n")
    elif human_point < comp_point:
        print(green("****!!!YOU LOOSE!!!****".center(columns)))
        print(green("****!!!BETTER LUCK NEXT TIME!!!****".center(columns)))
        print("\n")

    else:
        print(green("****!!!IT'S A DRAW!!!****".center(columns)))
        print(green("****!!!Why Don't You Try Again!!!****".center(columns)))
        print("\n")

    print("Do You Want To Play Again!!!")
    b = input("Enter Y for Yes & N for No :")
    print("\n")
    if b == 'Y':
        print(blue("Welcome Again!! Best Of Luck".center(columns)))
        print("\n")
        action()
    else:
        print(black("SAD TO SEE YOU GO!!".center(columns)))
        exit()

action()
