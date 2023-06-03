import tkinter
import random
def start():
    name = input("Enter your name >> ")
    money = random.randint(50,310)
    health = 100
    points = 0
    if len(name) > 0:
        game(name,money,health,points)
       

def game(name,money,health,points):
    window = tkinter.Tk()
    window.geometry("500x500")
    window.title("Game")
    Player_stat = tkinter.Frame(window)
    Player_stat.pack(anchor = "n", padx = 10)
    nameL = tkinter.Label(Player_stat, text = ("Name:",name), font=("TimesRoman, 10"))
    nameL.grid(row = 0, column= 0)
    moneyL = tkinter.Label(Player_stat, text = ("Money:",money), font=("TimesRoman, 10"))
    moneyL.grid(row = 0, column= 1)
    healthL = tkinter.Label(Player_stat, text = ("Health:",health), font=("TimesRoman, 10"))
    healthL.grid(row = 0, column= 2)
    pointsL = tkinter.Label(Player_stat, text = ("Points:",points), font=("TimesRoman, 10"))
    pointsL.grid(row = 0, column= 3)
    window.mainloop()


start()