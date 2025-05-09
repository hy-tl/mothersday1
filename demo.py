

import time
import sys


def clearscreen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def printbychar(msg, delay=0.05, maxlength=-1):
    i=0
    for char in msg:
        print(char,end="",flush=True)
        time.sleep(delay)
        i=i+1
        if maxlength!=-1 and i>=maxlength:
            i=0
            print()
    print()
    
def printbyword(msg, delay=0.05):
    for word in msg.split():
        print(word,end=" ",flush=True)
        time.sleep(delay)

def printbyline(msg, delay=0.05):
    for line in msg.split("\n"):
        print(line,flush=True)
        time.sleep(delay)
   
    
    
def test():
    clearscreen()
    message = "Hello, this is an animated message!"
    printbychar(message)

    message = "This is another message with a longer delay."
    printbychar(message, 0.1)

    message = "A very long wall of text text text text text text text text text text !"
    printbychar(message, 0.05, 20)
    
def mothersdaysimple():
    import time
    for i in range(5,0,-1):
        print("Hug in "+str(i)+"...")
        time.sleep(1)
    
    print("BIG HUG for Mummy!")
    print("I LOVE YOU MUM!!!")

def mothersdaytypewriter():
    clearscreen()
    printbyword("Ready in",1)
    printbychar("3... 2... 1...", 0.1)
    printbyline(
    """
             wWWWw               wWWWw
   vVVVv (___) wWWWw         (___)  vVVVv
   (___)  ~Y~  (___)  vVVVv   ~Y~   (___)
    ~Y~   \|    ~Y~   (___)    |/    ~Y~
    \|   \ |/   \| /  \~Y~/   \|    \ |/
   \\|// \\|// \\|/// \\|//  \\|// \\\|///
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """
    , 0.1)

    printbychar("Happy Mother's Day!",0.01)
    

def mothersdayturtle():
    # modified from this url:
    # https://www.geeksforgeeks.org/draw-a-flower-using-turtle-in-python/
    import turtle

    screen = turtle.Screen()
    screen.bgcolor("white")

    flower = turtle.Turtle()
    flower.speed(0)
    flower.pencolor("purple")
    flower.fillcolor("pink")

    # Draw a single petal
    def draw_petal():
        flower.begin_fill()
        flower.circle(100, 60)
        flower.left(120)
        flower.circle(100, 60)
        flower.left(120)
        flower.end_fill()

    # Draw all petals
    n=8
    for _ in range(n):
        draw_petal()
        flower.left(360/n)

    # flower center
    flower.penup()
    flower.goto(0, -40)
    flower.pendown()
    flower.color("orange")
    flower.fillcolor("yellow")
    flower.begin_fill()
    flower.circle(40)
    flower.end_fill()

    # Hide turtle and wait for click
    flower.hideturtle()
    flower.up()
    flower.goto(-100,-120)
    flower.color("orange")
    flower.write("Happy Mother's Day!", font=("Arial",16,"bold"))
    

    flower.goto(-100,-200)
    flower.color("black")
    flower.write("Click to continue", font=("Arial",8,"bold"))

    print("click on the image to continue")
    screen.exitonclick()
    



menu = [
    ["test", test],
    ["mother's day (simple))", mothersdaysimple],    
    ["mother's day (typewriter, using time.sleep))", mothersdaytypewriter],
    ["mother's day (turtle))", mothersdayturtle],    
]


# main menu
while True:
    try:
        # print menu with a default choice to quit
        print("\nChoose an option:")
        for i in range(len(menu)):
            print(f"{i} for",menu[i][0])
        print("-1 to quit")
        
        # enter choice
        choice = input("Enter choice:")
        choice = int(choice)
    
        if choice == -1:
            # handle quit
            break
        elif 0<=choice< len(menu):
            # handle valid choice
            menu[choice][1]()
            time.sleep(2) # add a small delay so that the end result can be seen without the menu1
        else:
            # handle bad choice
            raise ValueError()
    except:
        print("bad choice, try again\n")    
