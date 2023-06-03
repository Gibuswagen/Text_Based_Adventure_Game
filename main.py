import tkinter
import random
import os

#delete edit files
def deleteTxt():
    for n in range(1,4):
        os.remove("Room{}_Edit.txt".format(n))
    os.remove("Shop_Edit.txt")


#Function that asks a user for a name input and starts the game
def start():
    deleteTxt()
    name = input("Enter your name >> ")
    money = random.randint(50,310)
    health = 100
    points = 0
    if len(name) > 0:
        game(name,money,health,points)


#Function for later info use    
def readStages():
    for n in range(1,4):
        with open("Room{}.txt".format(n),"r") as origin, open("Room{}_Edit.txt".format(n),"w") as copy:
            for line in origin:
                copy.write(line)
    with open("Shop.txt".format(n),"r") as origin, open ("Shop_Edit.txt".format(n),"w") as copy:
        for line in origin:
            copy.write(line)


def game(name,money,health,points):

    #Read and copy stage infos
    readStages()

    #Create window
    window = tkinter.Tk()
    window.geometry("500x150")
    window.title("Game")

    #Player Info 
    Player_stat = tkinter.Frame(window)
    Player_stat.pack(anchor = "n", padx = 10)
    nameL = tkinter.Label(Player_stat, text = ("Name:",name), font=("TimesRoman, 10"))
    nameL.grid(row = 0, column= 0)
    moneyL = tkinter.Label(Player_stat, text = ("Money: $"+str(money)), font=("TimesRoman, 10"))
    moneyL.grid(row = 0, column= 1)
    healthL = tkinter.Label(Player_stat, text = ("Health:",health), font=("TimesRoman, 10"))
    healthL.grid(row = 0, column= 2)
    pointsL = tkinter.Label(Player_stat, text = ("Points:",points), font=("TimesRoman, 10"))
    pointsL.grid(row = 0, column= 3)
    
    #Room Buttons
    Levels = tkinter.Frame(window)
    Levels.pack(anchor="n", padx=10)
    r1_bt=tkinter.Button(Levels, text="Room 1")
    r1_bt.grid(row = 0, column = 0)
    r1_bt=tkinter.Button(Levels, text="Room 2")
    r1_bt.grid(row = 0, column = 1)
    r1_bt=tkinter.Button(Levels, text="Room 3")
    r1_bt.grid(row = 0, column = 2)
    r1_bt=tkinter.Button(Levels, text="Room 4")
    r1_bt.grid(row = 0, column = 3)
    r1_bt=tkinter.Button(Levels, text="Shop")
    r1_bt.grid(row = 0, column = 4)
    
    window.mainloop()
start()