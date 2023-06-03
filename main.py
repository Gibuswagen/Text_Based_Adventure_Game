import tkinter
import random

#Function that asks a user for a name input and starts the game
def start():
    global name
    name = input("Enter your name >> ")
    global money
    money = random.randint(50,310)
    global health
    health = 100
    global points
    points = 0
    global inventory
    inventory = {'Weapons':[],'Keys':[],'Armour':[]}
    if len(name) > 0:
        game(name,money,health,points)


#Function for later info use    
def readStages():
    for n in range(1,5):
        with open("Room{}.txt".format(n),"r") as origin, open("Room{}_Edit.txt".format(n),"w") as copy:
            for line in origin:
                copy.write(line)
    with open("Shop.txt".format(n),"r") as origin, open ("Shop_Edit.txt".format(n),"w") as copy:
        for line in origin:
            copy.write(line)

#Function that shows available weapons and allows to buy them
def weaponShop(info,inventory,money,moneyL):
    choice = 0
    while choice != "quit":    
        weapons=[]
        print("------------------------------------")
        w = 1
        for line in info:
            if "weapon{}".format(w) in line:
                s = line[8:]
                stats = s.split(",")
                weapons.append(stats)
                print(str(w)+".",stats[0].capitalize()+", "+"Damage: "+stats[1]+", "+"Price: $"+stats[2])      
                w+=1              
        print("------------------------------------")
        choice=(input("Which weapon would you like to buy?[1-"+str(len(weapons))+"]\nType 'quit' to go back\n"))
        if choice == "quit":
            break
        if int(choice) in range(1,len(weapons)+1):
            purchase = [weapons[int(choice)-1][0],int(weapons[int(choice)-1][1]),int(weapons[int(choice)-1][2])]
            if purchase in inventory['Weapons']:
                print("YOU ALREADY HAVE THIS ITEM")
            elif money >= purchase[2]:
                money -= purchase[2]
                inventory['Weapons'] += [purchase]
                print("ITEM PURCHASED SUCCESSFULLY")
                moneyL.configure(text = "Money: $"+str(money))
                
            else:
                print("NOT ENOUGH MONEY")
        else:
            print("TRY AGAIN")

#Function that shows available keys and allows to buy them    
def keyShop(info,inventory,money,moneyL):
    choice = 0
    while choice != "quit":
        keys = []
        print("------------------------------------")
        k = 1
        for line in info:
            if "key:" in line:
                s = line[4:]
                stats = s.split(",")
                keys.append(stats)
                print(str(k)+".","Type: "+stats[0]+", "+"Price: $"+stats[1])
                k+=1
        print("------------------------------------")
        choice=(input("Which key would you like to buy?[1-"+str(len(keys))+"]\nType 'quit' to go back\n"))
        if choice == "quit":
            break
        if int(choice) in range(1,len(keys)+1):
            purchase = [keys[int(choice)-1][0],int(keys[int(choice)-1][1])]
            if purchase in inventory['Keys']:
                print("YOU ALREADY HAVE THIS ITEM")
            elif money >= purchase[1]:
                money -= purchase[1]
                inventory['Keys'] += [purchase]
                print("ITEM PURCHASED SUCCESSFULLY")
                moneyL.configure(text = "Money: $"+str(money))        
            else:
                print("NOT ENOUGH MONEY")
        else:
            print("TRY AGAIN")

#Function that shows available armour and allows to buy them  
def armourShop(info,inventory,money,moneyL):
    choice = 0
    while choice != "quit":    
        armour=[]
        print("------------------------------------")
        w = 1
        for line in info:
            if "armour{}".format(w) in line:
                print(line)
                s = line[8:]
                stats = s.split(",")
                armour.append(stats)
                print(str(w)+"."+" Damage reduction: "+str(round(100-(100/int(stats[0])),2))+"%, "+"Price: $"+stats[1])      
                w+=1              
        print("------------------------------------")
        choice=(input("Which armour would you like to buy?[1-"+str(len(armour))+"]\nType 'quit' to go back\n"))
        if choice == "quit":
            break
        if int(choice) in range(1,len(armour)+1):
            purchase = [armour[int(choice)-1][0],int(armour[int(choice)-1][1])]
            if purchase in inventory['Armour']:
                print("YOU ALREADY HAVE THIS ITEM")
            elif money >= purchase[1]:
                money -= purchase[1]
                inventory['Armour'] += [purchase]
                print("ITEM PURCHASED SUCCESSFULLY")
                moneyL.configure(text = "Money: $"+str(money))
                
            else:
                print("NOT ENOUGH MONEY")
        else:
            print("TRY AGAIN")

# Function for shop
def Shop(moneyL,healthL,Levels):
    for button in Levels.winfo_children():
        button.configure(state='disable')
    #shop_bt.configure(state='disable')
    file = open("Shop_Edit.txt")
    print(file.readline().replace('\n', '')+", "+name)
    data = file.readlines()
    info=[]
    for line in data:
        info.append(line.strip())

    pin = 0
    while pin != "5":
        pin = input("How can I help? [1-5]\n1 >> Weapons\n2 >> Keys\n3 >> Healing Pads\n4 >> Armour\n5 >> Leave shop\n")
        if pin == "1":
            weaponShop(info,inventory,money,moneyL)
        elif pin == "2":
            keyShop(info,inventory,money,moneyL)
        elif pin == "3":
            pass
        elif pin =="4":
            armourShop(info,inventory,money,moneyL)

    print("YOU LEFT THE SHOP")
    for button in Levels.winfo_children():  
        button.configure(state='normal')
    file.close()
    


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
    r2_bt=tkinter.Button(Levels, text="Room 2")
    r2_bt.grid(row = 0, column = 1)
    r3_bt=tkinter.Button(Levels, text="Room 3")
    r3_bt.grid(row = 0, column = 2)
    r4_bt=tkinter.Button(Levels, text="Room 4")
    r4_bt.grid(row = 0, column = 3)
    shop_bt=tkinter.Button(Levels, text="Shop", command = lambda: Shop(moneyL,healthL,Levels))
    shop_bt.grid(row = 0, column = 4)
    
    window.mainloop()
start()