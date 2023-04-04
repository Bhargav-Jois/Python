import random
a=("Rock","Paper","Scissor")
numlist=(1,2,3)
def decor_win(func):
    def wrap():
        print("\n************")
        func()
        print("************\n")
    return wrap

@decor_win
def print_text_win():
    print("-->You Win :)")

def decor_lose(func):
    def wrap():
        print("\nxxxxxxxxxxxx")
        func()
        print("xxxxxxxxxxxx\n")
    return wrap

@decor_lose
def print_text_lose():
    print("-->You Lose :(")


def decor_draw_title(func):
    def wrap():
        print("\n=====================================")
        func()
        print("=====================================\n")
    return wrap

@decor_win
def print_text_tq():
    print("Thank you")

@decor_draw_title
def print_text_title():
    print("*******The Rock Paper Scissors*******")

print_text_title();
print("Rules:", end=" ")
print("This game has 3 objects (Rock, Paper and Scissor).Each object wins against one shape and loses to another. For instance, rock “crushes” scissors but is “covered” by paper, paper “covers” rock but is “cut” by scissors, and scissors is “crushed” by rock but “cuts” paper. The player who picks the stronger of the two objects is the winner. ")
while(1):
    cnum=random.choice(numlist)
    unum=int(input("\n1.Rock\n2.Paper\n3.Scissor\nChoose Your Object: "))
    if unum==cnum:
        if cnum<2:
            snum=1
        else:
            snum=-1
        cnum+=snum
    if cnum==1 and unum==3:
        print("Computer Choice: ", a[cnum-1])
        print("Your Choice: ",a[unum-1])
        print_text_lose();
    elif cnum==3 and unum==1:
        print("Computer Choice: ", a[cnum-1])
        print("Your Choice: ",a[unum-1])
        print_text_win();
    else:
        if unum<cnum:
            print("Computer Choice: ", a[cnum-1])
            print("Your Choice: ",a[unum-1])
            print_text_lose();
        elif unum>cnum:
            print("Computer Choice: ", a[cnum-1])
            print("Your Choice: ",a[unum-1])
            print_text_win();
        else:
            cnum=random.choice(numlist)
    leave=input("Do You Want To Play Again(y/n): ")
    if leave=='n':
        break
    elif leave=='y':
        continue
    else:
        print("Invalid Input")
        break
print_text_tq();
