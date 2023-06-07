import tkinter
import random
import sys

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


#clear entry if incorrect input
def clear_entry(user_entry):
    user_entry.delete(0, tkinter.END)

#Function that assigns name for per user entry input
def submitname(user_entry,output_label):
    if len(user_entry.get()) != 0:
        global nameInput
        nameInput = user_entry.get()
        nameWindow.destroy()
        
    else:
        output_label.configure(text = "Invalid username")
        clear_entry(user_entry)

#Function that asks a user for a name input and starts the game
def start():
    global nameWindow
    global nameInput
    nameWindow = tkinter.Tk()
    nameWindow.geometry("500x150")
    nameFrame = tkinter.Frame(nameWindow)
    nameFrame.pack()
    label= tkinter.Label(nameFrame,text="Enter your nickname", font=("TimesRoman, 10"))
    label.grid(row = 0, column = 0)
    user_entry = tkinter.Entry(nameFrame)
    user_entry.grid(row = 1, column = 0)
    output_label= tkinter.Label(nameFrame, font=("TimesRoman, 10"))
    output_label.grid(row = 2, column = 0)
    submit_bt=tkinter.Button(nameFrame, text="Submit", font=("TimesRoman, 10"), command = lambda: submitname(user_entry,output_label))
    submit_bt.grid(row = 3, column = 0)
    nameWindow.mainloop()   
    player = Player(nameInput,random.randint(50,310),100,0,{'Weapons':[],'Keys':[],'Armour':[]})
    if len(nameInput) > 0:
        game(player)

    # player = Player('Gibuswagen',10000,100,0,{'Weapons':[['knife',10,50]],'Keys':[],'Armour':[]})
    # game(player)


#Function for later info use    
def readStages():
    for n in range(1,5):
        with open("Room{}.txt".format(n),"r") as origin, open("Edit_Room{}.txt".format(n),"w") as copy:
            for line in origin:
                copy.write(line)
    with open("Shop.txt".format(n),"r") as origin, open ("Edit_Shop.txt".format(n),"w") as copy:
        for line in origin:
            copy.write(line)

#Function that shows available weapons and allows to buy them
def weaponShop(player,moneyL):
    choice = 0
    while choice != "quit":    
        info = readFile("Edit_Shop.txt")
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
    choice = 0
    while choice != "quit":
        info = readFile("Edit_Shop.txt")
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
    choice = 0
    while choice != "quit":    
        info = readFile("Edit_Shop.txt")
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
        info = readFile("Edit_Shop.txt")
        print("------------------------------------")
        for line in info:
            if "pad" in line:
                s = line[4:]
                stats = s.split(",")    
        if stats[0] == "0":
            print("Sorry, we are out of healing pads!")
            print("------------------------------------")
            return
        print("1.","Quantity: "+str(stats[0])+", "+"Health: +"+str(stats[1])+", "+"Price: "+str(stats[2]))
        print("------------------------------------")
        choice=input("Type 1 to buy a healing pad\nType 'quit' to go back\n")
        if choice == "quit":
            break
        if choice =="1":
            quantity = int(stats[0])
            cost = int(stats[2])
            hp = int(stats[1])
            if player.health == 100:
                print("YOU ARE ALREADY FULLY HEALED")
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
                    file = open("Edit_Shop.txt","w")
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
            print(str(counterA)+"."+"Armour: Damage reduction: "+str(round(100-(100/int(armour[0])),2))+"%, "+"Price: $"+str(armour[1]))
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
            player.money += int(purchase[-1])
            print("WEAPON SOLD SUCCESSFULLY")
            moneyL.configure(text = "Money: $"+str(player.money))
        elif int(choice) > counterW and int(choice) <= counterK:
            purchase = itemlist[int(choice)-1]
            keys = player.inventory['Keys']
            keys.remove(purchase)
            player.inventory['Keys']=keys
            player.money += int(purchase[-1])
            print("KEY SOLD SUCCESSFULLY")
            moneyL.configure(text = "Money: $"+str(player.money))
        elif int(choice) > counterK and int(choice) <= counterA:
            purchase = itemlist[int(choice)-1]
            armour = player.inventory['Armour']
            armour.remove(purchase)
            player.inventory['Armour']=armour
            player.money += int(purchase[-1])
            print("ARMOUR SOLD SUCCESSFULLY")
            moneyL.configure(text = "Money: $"+str(player.money))
        else:
            print("TRY AGAIN")
        

#This function is always called when file info needs to be read
def readFile(filename):
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
    info = readFile("Edit_Shop.txt")
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

def restartButton():
    window.destroy()
    start()
def checkState(player,Levels):
    if player.points < 0:
        for button in Levels.winfo_children():
            button.configure(state='disable')
        print("YOUR POINTS ARE BELOW 0!")
        print("GAME OVER!")
        choice = 0
        while choice not in ['1','2']:
            choice = input("Type 1 to Restart\nType 2 to Exit\n")
        if int(choice) == 1:
            window.destroy()
            start()
        elif int(choice) == 2:
            sys.exit()
    elif player.points >= 10:
        for button in Levels.winfo_children():
            button.configure(state='disable')
        print("YOU'VE REACHED 10 POINTS!")
        print("CONGRATULATIONS, YOU WON!")
        choice = 0
        while choice not in ['1','2']:
            choice = input("Type 1 to Restart\nType 2 to Exit\n")
        if int(choice) == 1:
            window.destroy()
            start()
        elif int(choice) == 2:
            sys.exit()
        
def GoToRoom(filename,player,Levels,moneyL,healthL,pointsL):
    if player.health == 0:
        print("YOU ARE NOT HEALED")
        return
    for button in Levels.winfo_children():
        button.configure(state='disable')
    room=readFile(filename)
    print("\n"+room[0]+"\n"+room[1]+"\n")

    for idx, line in enumerate(room):
        if "# Enemy" in line:
            enemystats = room[idx+1].split(",")
            if int(enemystats[2]) == 0:
                enemystats=[]

    if len(enemystats) != 0:
        print("Enemy encountered!")
        print("Name: "+enemystats[0]+" Damage: "+enemystats[1]+" Health: "+enemystats[2])
        action = input("Type 1 to Fight\nType 2 to Run\n")
        if action == "1":
            if len(player.inventory["Weapons"]) == 0:
                print("YOU HAVE NO WEAPON TO FIGHT...\nYOU RAN AWAY\n")
                for button in Levels.winfo_children():  
                    button.configure(state='normal')
                return
            else:
                weapon=[]
                armour=[]
                counterW = 0
                print("------------------------------------")
                print("Weapons: ")
                for weapon in player.inventory['Weapons']:
                    counterW += 1
                    print(str(counterW)+".",weapon[0].capitalize()+", "+"Damage: "+str(weapon[1])+", "+"Price: $"+str(weapon[2]))
                print("------------------------------------")
                wc = 0
                while wc < 1 or wc > len(player.inventory['Weapons']):
                    wc = int(input("Choose your weapon[1-"+str(len(player.inventory['Weapons']))+"]\n"))
                weapon = player.inventory['Weapons'][wc-1]

                if len(player.inventory['Armour']) != 0:
                    counterA = 0
                    print("------------------------------------")
                    print("Armour: ")
                    for armour in player.inventory['Armour']:
                        counterA +=1
                        print(str(counterA)+"."+" Damage reduction: "+str(round(100-(100/int(armour[0])),2))+"%, "+"Price: $"+str(armour[1]))
                    print("------------------------------------")
                    ac = -1
                    while ac < 0 or ac > len(player.inventory['Armour']):
                        ac = int(input("Choose your armour[0 - None][1-"+str(len(player.inventory['Armour']))+"]\n"))
                    if ac == 0:
                        armour = [1]
                    else:
                        armour = player.inventory['Armour'][ac-1]
                else:
                    armour = [1]

                enemyHP = int(enemystats[2])
                enemyDMG = int(enemystats[1])/int(armour[0])

                while enemyHP > 0 and player.health > 0:   
                    enemyHP -= int(weapon[1])
                    player.health = round(player.health - enemyDMG)

                if player.health <= 0:
                    player.health = 0
                    healthL.configure(text = "Health: "+str(player.health))
                    player.points -= 2
                    checkState(player,Levels)
                    pointsL.configure(text = "Points: "+str(player.points))
                    player.inventory['Weapons'].remove(weapon)
                    if armour[0] != 1:
                        player.inventory['Armour'].remove(armour)
                    enemystats[2] = str(enemyHP)
                    file = open(filename,"w")
                    for idx,line in enumerate(room):
                        room[idx] += "\n"
                        if "# Enemy" in line:
                            newstats = ",".join(enemystats)
                            room[idx+1] = newstats
                        file.write(room[idx])
                        room[idx] = room[idx].replace('\n','')
                    file.close()
                    print("YOU LOST")
                    for button in Levels.winfo_children():  
                        button.configure(state='normal')
                    return
                elif enemyHP <= 0:
                    print("YOU DEFEATED "+enemystats[0].upper())
                    healthL.configure(text = "Health: "+str(player.health))
                    enemystats[2] = str(0)
                    #Change HP of enemy to 0 in file
                    file = open(filename,"w")
                    for idx,line in enumerate(room):
                        room[idx] += "\n"
                        if "# Enemy" in line:
                            newstats = ",".join(enemystats)
                            room[idx+1] = newstats
                        file.write(room[idx])
                        room[idx] = room[idx].replace('\n','')
                    file.close()
                    #Receive rewards for killing an enemy
                    for idx,line in enumerate(room):
                        if "# Point" in line:
                            player.points += int(room[idx+1])
                            pointsL.configure(text = "Points: "+str(player.points))
                            print(room[idx+1]+" POINTS RECEIVED")
                            checkState(player,Levels)
                        if "# Weapon" in line:
                            weapon = room[idx+1].split(",")
                            player.inventory['Weapons'] += [weapon]
                            print("NEW WEAPON RECEIVED: "+"Name: "+weapon[0]+", Damage: "+weapon[1]+", Price: $"+weapon[2])
                        if "# Money" in line:
                            reward = int(room[idx+1])
                            player.money += reward
                            moneyL.configure(text = "Money: $"+str(player.money))
                            print("$"+str(reward)+" RECEIVED")
                        if "# HealingPad" in line:
                            print("YOU FOUND HEALING PADS")
                            quantity = int(room[idx+1])
                            if player.health + (quantity * 50) > 100:
                                player.health = 100
                                healthL.configure(text = "Health: "+str(player.health))
                                print("YOU ARE FULLY HEALED")
                            else:
                                player.health += (quantity * 50)
                                healthL.configure(text = "Health: "+str(player.health))
                                print("YOU HEALED 50 HEALTH")
                        if "# Key" in line:
                            k = room[idx+1].split(",")
                            player.inventory['Keys'] += [k]
                            print("YOU FOUND A KEY")
                            print("Type: "+k[0]+", "+"Price: $"+k[1])

                        if "# Treasure" in line:
                            chest = room[idx+1].split(",")
                            choice = 0
                            while choice not in ['1','2']:
                                choice = input("You see treasure chest!\nType 1 to try to open it [Key type:"+chest[0]+"]\nType 2 to ignore\n")
                            if choice == "1":
                                if len(player.inventory['Keys']) == 0:
                                    print("You don't have keys in inventory.")
                                    break
                                for key in player.inventory['Keys']:
                                    if key[0] == chest[0]:
                                        print("You used a matching key!")
                                        player.inventory['Keys'].remove(key)
                                        player.points += int(chest[1])
                                        print(chest[1]+" POINTS RECEIVED")
                                        pointsL.configure(text = "Points: "+str(player.points))
                                        checkState(player,Levels)
                                        file = open(filename,"w")
                                        for line in room:
                                            line += "\n"
                                            if "# Treasure" in line:
                                                line = "\n"
                                            file.write(line)
                                            line = line.replace('\n','')
                                        file.close()
                                        break
                                    else:
                                        print("Put key didn't work...")
                            elif choice == "2":
                                print("You chose to ignore the treasure chest.")
                    for button in Levels.winfo_children():
                        button.configure(state='normal')
                    return
        elif action == "2":
            print("YOU RAN\n")
            for button in Levels.winfo_children():  
                button.configure(state='normal')
            return
        
    elif len(enemystats) == 0:
        print("ENEMY OF THIS REGION HAS ALREADY BEEN DEFEATED\n")
        for idx,line in enumerate(room):
            if "# Treasure" in line:
                chest = room[idx+1].split(",")
                choice = 0
                while choice not in ['1','2']:
                    choice = input("You see treasure chest!\nType 1 to try to open it [Key type:"+chest[0]+"]\nType 2 to ignore\n")
                if choice == "1":
                    if len(player.inventory['Keys']) == 0:
                        print("You don't have keys in inventory.")
                        break
                    for key in player.inventory['Keys']:
                        if key[0] == chest[0]:
                            print("You used a matching key!")
                            player.inventory['Keys'].remove(key)
                            player.points += int(chest[1])
                            print(chest[1]+" POINTS RECEIVED")
                            pointsL.configure(text = "Points: "+str(player.points))
                            checkState(player,Levels)
                            file = open(filename,"w")
                            for line in room:                
                                line += "\n"
                                if "# Treasure" in line:
                                    line = "\n"
                                file.write(line)
                                line = line.replace('\n','')
                            file.close()
                            break
                        else:
                            print("Put key didn't work...")
                elif choice == "2":
                    print("You chose to ignore the treasure chest.")
        for button in Levels.winfo_children():
            button.configure(state='normal')
        return

def game(player):

    #Read and copy stage infos
    readStages()

    #Create window
    global window
    window = tkinter.Tk()
    window.geometry("500x150")
    window.title("Game")

    #Player Info 
    Player_stat = tkinter.Frame(window)
    Player_stat.pack(anchor = "n", padx = 10, pady=10)
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
    Levels.pack(anchor="n", padx=10,pady=10)
    r1_bt=tkinter.Button(Levels, text="Room 1", command = lambda: GoToRoom("Edit_Room1.txt",player,Levels,moneyL,healthL,pointsL))
    r1_bt.grid(row = 0, column = 0)
    r2_bt=tkinter.Button(Levels, text="Room 2", command = lambda: GoToRoom("Edit_Room2.txt",player,Levels,moneyL,healthL,pointsL))
    r2_bt.grid(row = 0, column = 1)
    r3_bt=tkinter.Button(Levels, text="Room 3", command = lambda: GoToRoom("Edit_Room3.txt",player,Levels,moneyL,healthL,pointsL))
    r3_bt.grid(row = 0, column = 2)
    r4_bt=tkinter.Button(Levels, text="Room 4", command = lambda: GoToRoom("Edit_Room4.txt",player,Levels,moneyL,healthL,pointsL))
    r4_bt.grid(row = 0, column = 3)
    shop_bt=tkinter.Button(Levels, text="Shop", command = lambda: Shop(moneyL,healthL,Levels,player))
    shop_bt.grid(row = 0, column = 4)

    #Restart Button
    restart_bt = tkinter.Button(window, text = "Restart", command = restartButton)
    restart_bt.pack(anchor="n") 
    window.mainloop()

start()