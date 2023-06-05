import tkinter
import random


# class Player storing all the player stats
class Player:
    def __init__(self,name,money,health,points,inventory):
        self.name = name
        self.money = money
        self.health = health
        self.points = points
        self.inventory = inventory
    def showInventory(self):
        counterW=0
        counterK=0
        counterA=0
        print("------------------------------------")
        print("Weapons: ")
        for weapon in self.inventory['Weapons']:
            counterW += 1
            print(str(counterW)+".",weapon[0].capitalize()+", "+"Damage: "+str(weapon[1])+", "+"Price: $"+str(weapon[2]))
        print("Keys: ")
        for key in self.inventory['Keys']:
            counterK += 1
            print(str(counterK)+".","Type: "+str(key[0])+", "+"Price: $"+str(key[1]))
        print("Armour: ")
        for armour in self.inventory['Armour']:
            counterA +=1
            print(str(counterA)+"."+" Damage reduction: "+str(round(100-(100/int(armour[0])),2))+"%, "+"Price: $"+str(armour[1]))
        print("------------------------------------")



#Function that asks a user for a name input and starts the game
def start():
    name = input("Enter your name >> ")
    player = Player(name,10000,20,0,{'Weapons':[],'Keys':[],'Armour':[]})
    if len(name) > 0:
        game(player)


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
def weaponShop(player,moneyL):
    info = readShop("Shop_Edit.txt")
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
                w+=1
        weapons.sort(key= lambda x: int(x[-1]))
        for c in range(len(weapons)):
            print(str(c+1)+".",weapons[c][0].capitalize()+", "+"Damage: "+weapons[c][1]+", "+"Price: $"+weapons[c][2])

        print("------------------------------------")
        choice=(input("Which weapon would you like to buy?[1-"+str(len(weapons))+"]\nType 'quit' to go back\n"))
        if choice == "quit":
            break
        if int(choice) in range(1,len(weapons)+1):
            purchase = [weapons[int(choice)-1][0],int(weapons[int(choice)-1][1]),int(weapons[int(choice)-1][2])]
            if purchase in player.inventory['Weapons']:
                print("YOU ALREADY HAVE THIS ITEM")
            elif player.money >= purchase[2]:
                player.money -= purchase[2]
                player.inventory['Weapons'] += [purchase]
                print("ITEM PURCHASED SUCCESSFULLY")
                moneyL.configure(text = "Money: $"+str(player.money))   
            else:
                print("NOT ENOUGH MONEY")
        else:
            print("TRY AGAIN")

#Function that shows available keys and allows to buy them    
def keyShop(player,moneyL):
    info = readShop("Shop_Edit.txt")
    choice = 0
    while choice != "quit":
        keys = []
        print("------------------------------------")
        k = 1
        for line in info:
            if "key" in line:
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
            if purchase in player.inventory['Keys']:
                print("YOU ALREADY HAVE THIS ITEM")
            elif player.money >= purchase[1]:
                player.money -= purchase[1]
                player.inventory['Keys'] += [purchase]
                print("ITEM PURCHASED SUCCESSFULLY")
                moneyL.configure(text = "Money: $"+str(player.money))        
            else:
                print("NOT ENOUGH MONEY")
        else:
            print("TRY AGAIN")

#Function that shows available armour and allows to buy them  
def armourShop(player,moneyL):
    info = readShop("Shop_Edit.txt")
    choice = 0
    while choice != "quit":    
        armour=[]
        print("------------------------------------")
        w = 1
        for line in info:
            if "armour{}".format(w) in line:
                s = line[8:]
                stats = s.split(",")
                armour.append(stats)      
                w+=1
        armour.sort(key= lambda x: int(x[-1]))
        for c in range(len(armour)):
            print(str(c+1)+"."+" Damage reduction: "+str(round(100-(100/int(armour[c][0])),2))+"%, "+"Price: $"+armour[c][1])              
        print("------------------------------------")
        choice=input("Which armour would you like to buy?[1-"+str(len(armour))+"]\nType 'quit' to go back\n")
        if choice == "quit":
            break
        if int(choice) in range(1,len(armour)+1):
            purchase = [armour[int(choice)-1][0],int(armour[int(choice)-1][1])]
            if purchase in player.inventory['Armour']:
                print("YOU ALREADY HAVE THIS ITEM")
            elif player.money >= purchase[1]:
                player.money -= purchase[1]
                player.inventory['Armour'] += [purchase]
                print("ITEM PURCHASED SUCCESSFULLY")
                moneyL.configure(text = "Money: $"+str(player.money))
                
            else:
                print("NOT ENOUGH MONEY")
        else:
            print("TRY AGAIN")


#Function to buy healing pads
def healingPads(player,healthL,moneyL):
    choice = 0
    while choice != "quit":   
        info = readShop("Shop_Edit.txt") 
        print("------------------------------------")
        for line in info:
            if "pad" in line:
                s = line[4:]
                stats = s.split(",")    
        print("1.","Quantity: "+str(stats[0])+", "+"Health: +"+str(stats[1])+", "+"Price: "+str(stats[2]))
        if stats[0] == "0":
            print("Sorry, we are out of healing pads!")
            print("------------------------------------")
            return
        print("------------------------------------")
        choice=input("Type 1 to buy a healing pad\nType 'quit' to go back\n")
        if choice == "quit":
            break
        if choice =="1":
            quantity = int(stats[0])
            cost = int(stats[2])
            hp = int(stats[1])
            if player.health == 100:
                print("You already fully healed")
                return
            elif player.health < 100:
                if player.money >= cost:
                    player.money -= cost
                    if player.health + hp > 100:
                        player.health = 100
                    else:
                        player.health += hp
                    moneyL.configure(text = "Money: $"+str(player.money))
                    healthL.configure(text = "Health: "+str(player.health))
                    file = open("Shop_Edit.txt","w")
                    for line in info:
                        line += "\n"
                        if "pad:" in line:
                            line = line.replace(":"+str(quantity)+",",":"+str(quantity-1)+",")
                        file.write(line)
                        line=line.replace('\n','')
                    file.close()
                else:
                    print("NOT ENOUGH MONEY")
        else:
            print("TRY AGAIN")
    

#Function to sell your items in the inventory
def sellItems(player,moneyL):
    choice = 0
    while choice != "quit":
        counterW=0
        counterK=0
        counterA=0
        itemlist = []
        print("------------------------------------")
        for weapon in player.inventory['Weapons']:
            counterW += 1
            print(str(counterW)+".",weapon[0].capitalize()+", "+"Damage: "+str(weapon[1])+", "+"Price: $"+str(weapon[2]))
            itemlist.append(weapon)
        counterK = counterW
        for key in player.inventory['Keys']:
            counterK += 1
            print(str(counterK)+".","Type: "+str(key[0])+", "+"Price: $"+str(key[1]))
            itemlist.append(key)
        counterA = counterK
        for armour in player.inventory['Armour']:
            counterA +=1
            print(str(counterA)+"."+" Damage reduction: "+str(round(100-(100/int(armour[0])),2))+"%, "+"Price: $"+str(armour[1]))
            itemlist.append(armour)
        print("------------------------------------")
        if len(itemlist) == 0:
            print("YOU HAVE NO ITEMS TO SELL")
            break
        choice = input("Which item would you like to sell?[1-"+str(counterA)+"]\nType 'quit' to go back\n")
        if choice == "quit":
            break
        if int(choice) > 0 and int(choice) <= counterW:
            purchase = itemlist[int(choice)-1]
            weapons = player.inventory['Weapons']
            weapons.remove(purchase)
            player.inventory['Weapons']=weapons
            player.money += purchase[-1]
            print("WEAPON SOLD SUCCESSFULLY")
            moneyL.configure(text = "Money: $"+str(player.money))
        elif int(choice) > counterW and int(choice) <= counterK:
            purchase = itemlist[int(choice)-1]
            keys = player.inventory['Keys']
            keys.remove(purchase)
            player.inventory['Keys']=keys
            player.money += purchase[-1]
            print("KEY SOLD SUCCESSFULLY")
            moneyL.configure(text = "Money: $"+str(player.money))
        elif int(choice) > counterK and int(choice) <= counterA:
            purchase = itemlist[int(choice)-1]
            armour = player.inventory['Armour']
            armour.remove(purchase)
            player.inventory['Armour']=armour
            player.money += purchase[-1]
            print("ARMOUR SOLD SUCCESSFULLY")
            moneyL.configure(text = "Money: $"+str(player.money))
        else:
            print("TRY AGAIN")
        

    
def readShop(filename):
    file = open(filename)
    data = file.readlines()
    info=[]
    for line in data:
        info.append(line.strip())
    return info

# Function for shop
def Shop(moneyL,healthL,Levels,player):
    for button in Levels.winfo_children():
        button.configure(state='disable')
    info = readShop("Shop_Edit.txt")
    print(info[0]+", "+player.name)

    pin = 0
    while pin != "6":
        pin = input("How can I help? [1-5]\n1 >> Weapons\n2 >> Keys\n3 >> Healing Pads\n4 >> Armour\n5 >> Sell items\n6 >> Leave shop\n")
        if pin == "1":
            weaponShop(player,moneyL)
        elif pin == "2":
            keyShop(player,moneyL)
        elif pin == "3":
            healingPads(player,healthL,moneyL)
        elif pin =="4":
            armourShop(player,moneyL)
        elif pin =="5":
            sellItems(player,moneyL)

    print("YOU LEFT THE SHOP")
    for button in Levels.winfo_children():  
        button.configure(state='normal')
    


def game(player):

    #Read and copy stage infos
    readStages()

    #Create window
    window = tkinter.Tk()
    window.geometry("500x150")
    window.title("Game")

    #Player Info 
    Player_stat = tkinter.Frame(window)
    Player_stat.pack(anchor = "n", padx = 10)
    nameL = tkinter.Label(Player_stat, text = ("Name:",player.name), font=("TimesRoman, 10"))
    nameL.grid(row = 0, column= 0)
    moneyL = tkinter.Label(Player_stat, text = ("Money: $"+str(player.money)), font=("TimesRoman, 10"))
    moneyL.grid(row = 0, column= 1)
    healthL = tkinter.Label(Player_stat, text = ("Health:",player.health), font=("TimesRoman, 10"))
    healthL.grid(row = 0, column= 2)
    pointsL = tkinter.Label(Player_stat, text = ("Points:",player.points), font=("TimesRoman, 10"))
    pointsL.grid(row = 0, column= 3)
    inv_bt = tkinter.Button(window, text="Inventory", command = player.showInventory)
    inv_bt.pack(anchor="n")    
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
    shop_bt=tkinter.Button(Levels, text="Shop", command = lambda: Shop(moneyL,healthL,Levels,player))
    shop_bt.grid(row = 0, column = 4)
    
    window.mainloop()
start()