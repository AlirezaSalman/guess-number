from random import randint

win = True
a = 0
b = 100

while(win):
    guess = randint(a, b)
    client_act = input(f" is {guess} your number? (B => Bigger, S => Smaller, Y => Yes) ")
    if client_act.upper() == "B":
        a = guess + 1
    elif client_act.upper() == "S":
        b =  guess - 1
    elif client_act.upper() == "Y":
        win = False
        print("good game!")
    else: 
        print("incorrect command!")
        win = False