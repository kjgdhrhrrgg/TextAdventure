#!/usr/bin/env python
# -*- coding: utf-8 -*-


from CharacterClass import Character
from ItemClass import Item
from Essentials import Writing_animation_Line
from Essentials import Writing_animation_Print
from Essentials import Clearscreen
from Essentials import Title
from Essentials import Loading_Screen
from Essentials import userpw
from Essentials import usernumber
from Essentials import bcl
from Essentials import fcl
from Essentials import Login
from Essentials import Optionen_Screen
from Essentials import Menu_Screen
from Essentials import ASCII_pic
from random import uniform
from random import sample
import uuid
import json
import time
import os
import platform

########################### list etc. ######################################################

global sg
global eg
global ag
global beag
global bsg
global itemlist
global characterlist
global titlename


titlename = "kjgdhrhrrgg's Labyrinth"
sg = ["os1", "os2", "os3","os4","os5","gs1","bs1","bs2","bs3","bs4","bs5","bs6","ps1","ps2","ps3","ps4","ps5","ps6","ps7","ps8"]
eg = ["oe1r", "ge1l", "be1u", "pe1u"]
ag = ["oe1l","ge1r","be1d","pe1d"]
beag = []
bsg = []
itemlist = []
characterlist = []
cheatcode = False



##ASCII FONT: THIS (http://patorjk.com/software/taag/#p=display&f=THIS&t=kjgdhrhrrgg)


######################################## LOADING STUFF ##################################


def Jsonfile_Loading():

    with open("config.json") as jsonfile1:
        
        global cfg
        cfg = json.load(jsonfile1)
    
    with open("map.json") as jsonfile2:
        
        global map
        map = json.load(jsonfile2) 

    with open("item.json") as jsonfile3:
        
        global item
        item = json.load(jsonfile3)
        
def Item_Loading(sg):

    itemlocation = sample(sg,1)
    global Schlüssel1
    global Schlüssel2
    global Schlüssel3
    global Schwert
    Schlüssel1 = Item(item["Item1"]["name"], item["Item1"]["info"], item["Item1"]["hp"],item["Item1"]["atk"],item["Item1"]["def"],item["Item1"]["itemlocation"])
    Schlüssel2 = Item(item["Item2"]["name"], item["Item2"]["info"], item["Item2"]["hp"],item["Item2"]["atk"],item["Item2"]["def"],item["Item2"]["itemlocation"])
    Schlüssel3 = Item(item["Item3"]["name"], item["Item3"]["info"], item["Item3"]["hp"],item["Item3"]["atk"],item["Item3"]["def"],item["Item3"]["itemlocation"])
    Schwert = Item(item["Item4"]["name"],item["Item4"]["info"], item["Item4"]["hp"], item["Item4"]["atk"], item["Item4"]["def"], itemlocation)
    itemlist.append(Schlüssel1)
    itemlist.append(Schlüssel2)
    itemlist.append(Schlüssel3)
    itemlist.append(Schwert)
    Loading_Screen("Items", len(itemlist))

def Inventory_Loading():

    global invs
    global invc1
    global invc2
    global invc3
    invs = {1: "",2: "", 3: "", 4: ""}
    invc1 = {1: "", 2: Schlüssel1, 3: "", 4: ""}
    invc2 = {1: Schlüssel2, 2: "", 3: "", 4: ""}
    invc3 = {1: Schlüssel3, 2: "", 3: "", 4: ""}

def Character_Loading():

    global spieler
    global character1
    global character2
    global character3
    character3 = Character(x3, character3HP, character3ATK, character3DEF, "or1", invc3)
    character2 = Character(x2, character2HP, character2ATK, character2DEF, "gr1", invc2)
    character1 = Character(x1, character1HP, character1ATK, character1DEF, "pr1", invc1)
    spieler = Character(x0, cfg["spieler"]["hp"], cfg["spieler"]["atk"], cfg["spieler"]["def"], "vr1d", invs)
    characterlist.append(spieler)
    characterlist.append(character1)
    characterlist.append(character2)
    characterlist.append(character3)
    Loading_Screen("Charaktere", len(characterlist))

################################### ESSENTIALS ######################################


def Countsystem():
    
    #besuchte eingänge und ausgänge zählen
    if spieler.position in eg or ag:

        if spieler.position not in beag:
                
            beag.append(spieler.position)
            
    if spieler.position in sg:

        if spieler.position not in bsg:

            bsg.append(spieler.position)



#################################### ENDE ############################################



def Verloren():
    
    ende = "verloren"
    End_Screen(ende)

def Gewonnen():

    ende = "gewonnen"
    End_Screen(ende)


############################### ITEM INTERAKTIONEN ##################################


def Get_Item(gegner):

    new_Item = ""
    
    for gegner_slot, existing_Item in gegner.inventory.items():
        
        if existing_Item != "":

            new_Item = existing_Item
            new_Item.position = gegner.position
            gegner.inventory[gegner_slot] = ""
            Add_Item(new_Item)
            break

def Add_Item(new_Item):

    Writing_animation_Print(new_Item.beschreibung)
    
    for spieler_slot, spieler_Item in spieler.inventory.items():

        if spieler_Item == "":

            min_spieler_slot = min(spieler.inventory, key=spieler.inventory.get)

            if spieler.inventory[min_spieler_slot] == "":

                spieler.inventory[min_spieler_slot] = new_Item.name
                Schwert.position == ""
                spieler.AddItem(new_Item)
                break
    
    time.sleep(5)
    


######################################## BEWEGUNG ###########################################


def Ziel(np):
    
    spieler.position = np 
    Position()

def Zielcheck(np):

    #Check, ob man hier entlanglaufen kann
    if np == "":
        
        Writing_animation_Line(44)
        Bewegung()     

def Eingangscheck():

    if spieler.position in eg:

        if spieler.position == "pe1u":

            Writing_animation_Line(42)
            Writing_animation_Line(3)
            eabfrage1 = input(">").lower()

            if eabfrage1 == "j":
            
                spieler.position = map[spieler.position]["OBEN"]
                Position()

            elif eabfrage1 == "n":

                spieler.position = map[spieler.position]["UNTEN"]
                Position()
                
            else:
                
                Writing_animation_Line(2)
                Eingangscheck()
                
        if spieler.position == "oe1r":

            if Schlüssel1.name and Schlüssel2.name in invs:

                Writing_animation_Line(42)
                Writing_animation_Line(3)
                eabfrage2 = input(">").lower()

                if eabfrage2 == "j":
            
                    spieler.position = map[spieler.position]["OBEN"]
                    Position()

                elif eabfrage2 == "n":

                    spieler.position = map[spieler.position]["UNTEN"]
                    Position()

                else:
                
                    Writing_animation_Line(2)
                    Eingangscheck()
                
            else:

                Writing_animation_Line(43)
                spieler.position = map[spieler.position]["UNTEN"]
                Position()

        if spieler.position == "ge1l":

            if Schlüssel1.name in invs:

                Writing_animation_Line(42)
                Writing_animation_Line(3)
                eabfrage3 = input(">").lower()

                if eabfrage3 == "j":
            
                    spieler.position = map[spieler.position]["OBEN"]
                    Position()

                elif eabfrage3 == "n":

                    spieler.position = map[spieler.position]["UNTEN"]
                    Position()
                
                else:
                
                    Writing_animation_Line(2)
                    Eingangscheck()

            else:

                Writing_animation_Line(43)
                spieler.position = map[spieler.position]["UNTEN"]
                Position()

        if spieler.position == "br1u":

            if Schlüssel1.name and Schlüssel2.name and Schlüssel3.name in invs:

                Writing_animation_Line(40)
                Writing_animation_Line(3)
                eabfrage4 = input(">").lower()

                if eabfrage4 == "j":
            
                    spieler.position = map[spieler.position]["OBEN"]
                    Position()

                elif eabfrage4 == "n":

                    spieler.position = map[spieler.position]["UNTEN"]
                    Position()
                
                else:
                
                    Writing_animation_Line(2)
                    Eingangscheck()

            else:

                Writing_animation_Line(43)
                spieler.position = map[spieler.position]["UNTEN"]
                Position()

def Bewegung():
    import pdb
    pdb.set_trace()
    #check, ob man sich am eingang befindet
    Eingangscheck()
    
    #check, in welche richtung man laufen kann (keine eigene funktion, wegen den variablen)  
    v = "(v)orne \n"
    r = "(r)echts \n"
    l = "(l)inks \n"
    h = "(h)inten \n"
    if map[spieler.position]["OBEN"] == "":
       
       v = ""
    
    if map[spieler.position]["RECHTS"] == "":
        
        r = ""
    
    if map[spieler.position]["LINKS"] == "":
        
        l = ""
    
    if map[spieler.position]["UNTEN"] == "":
    
        h = ""
    
    #Bewegung beginnt hier:
    Writing_animation_Print("Wohin möchtest du hin? \n" + v + r + h + l)
    frage = input(">").lower()
    
    if frage == "v":
    
        np = map[spieler.position]["OBEN"]
        Zielcheck(np)
        Ziel(np)
    
    elif frage == "r":
    
        np = map[spieler.position]["RECHTS"]
        Zielcheck(np)
        Ziel(np)
    
    elif frage == "h":
        
        np = map[spieler.position]["UNTEN"] 
        Zielcheck(np)
        Ziel(np)
    
    elif frage == "l":
    
        np = map[spieler.position]["LINKS"]    
        Zielcheck(np)
        Ziel(np)

    else:
        
        Writing_animation_Line(2)
        Bewegung()

def Position():
    
    Clearscreen()
    Countsystem()
    Title(titlename + ", " + map[spieler.position]["INFO"])
    if spieler.position == character1.position:

        Writing_animation_Print(map[spieler.position]["BESCHREIBUNG"])
        Kampf(character1)   
    
    elif spieler.position == character2.position:
        
        Writing_animation_Print(map[spieler.position]["BESCHREIBUNG"])
        Kampf(character2)

    elif spieler.position == character3.position:


        Writing_animation_Print(map[spieler.position]["BESCHREIBUNG"])
        Kampf(character3)
    
    elif spieler.position == "br1":

        Writing_animation_Print(map[spieler.position]["BESCHREIBUNG"])
        Gewonnen()


    elif spieler.position == Schwert.position:

        new_Item = Schwert
        Add_Item(new_Item)
        Bewegung()
    
    else:
        
        Bewegung()
    

######################################## KAMPF ##################################################




def HP_check(gegner):

    if int(spieler.HP) <= 0 or int(gegner.HP) <= 0:
        
        if int(spieler.HP) <= 0:
            
            Writing_animation_Line(32)
            Verloren()
        
        elif int(gegner.HP) <= 0:
            
            Writing_animation_Print("Du hast " + gegner.name + " getötet! \n")
            Get_Item(gegner)
            gegner.position = ""
            spieler.position = map[spieler.position]["UNTEN"]
            Position()

def Loop(gegner):
    
    ASCII_pic("Kampf.txt")
    HP_check(gegner) 
    Writing_animation_Line(32)
    auswahl = input(">").lower()

    if auswahl == "a" :
        
        Writing_animation_Print("Du greifst " + gegner.name + " an! \n")
        spieler.Angreifen(gegner)
        HP_check(gegner)
        x = uniform(0,10)
        
        while int(x) >= int(attackchance):
                    
            Writing_animation_Print(gegner.name + " greift nicht zurück. \n")
            Writing_animation_Line(33)
            Loop(gegner)

        Writing_animation_Print(gegner.name + " greift dich an. \n")
        gegner.Angreifen(spieler)
        HP_check(gegner)    
        Loop(gegner)
        
    elif auswahl == "f":
            
        y = uniform(0,10)
            
        while y <= 9 :
                
            Writing_animation_Line(35)
            x = uniform(0,10)        

            while int(x) >= int(attackchance):
                    
                Writing_animation_Print(gegner.name + " greift nicht zurück. \n")
                Writing_animation_Line(33)
                Loop(gegner)                   
            Loop(gegner)

        Writing_animation_Line(36)
        spieler.position = map[spieler.position]["UNTEN"]
        Position()
        
    elif auswahl == str(userpw):

        global cheatcode
        Writing_animation_Line(38)
        spieler.HP = 9999
        spieler.ATK = 9999
        spieler.DEF = 9999
        cheatcode = True
        Loop(gegner)
    
    else:
            
        Writing_animation_Line(2)
        Loop(gegner)

def Kampf(gegner):
    
    Title("Kampf")
    ASCII_pic("Kampf.txt")
    Writing_animation_Print("Du befindest dich jetzt im Kampf mit " + gegner.name + ". \n")
    Loop(gegner)


################################## SPIEL EINSTELLUNGEN ###########################################

        
def Auswahl(auswahl):
    
    global x0
    global x1
    global x2
    global x3
    
    Clearscreen()
    Title("Auswahlmodus")

    if auswahl == 0:
        
        Writing_animation_Line(18)
        x0 = input("Dein Spielername: ")
        Auswahl(1)
        
    elif auswahl == 1:
        
        Writing_animation_Line(20)
        Writing_animation_Line(3)
        a1 = input(">").lower()
        
        if a1 == "j":
            
            Writing_animation_Line(19)
            x1 = input("Name: ")
            Auswahl(2)
        
        elif a1 == "n":
            
            x1 = "Isaac"
            Auswahl(2)
        
        else:
            
            Writing_animation_Line(2)
            Auswahl(1)
    
    elif auswahl == 2:
        
        Writing_animation_Line(21)
        Writing_animation_Line(3)
        a2 = input(">").lower()
        
        if a2 == "j":
            
            Writing_animation_Line(21)
            x2 = input("Name: ")
            Auswahl(3)     
        
        elif a2 == "n":

            x2 = "Kaos"
            Auswahl(3)
        
        else:
            
            Writing_animation_Line(2)
            Auswahl(2)
    
    elif auswahl == 3:
        
        Writing_animation_Line(22)
        Writing_animation_Line(3)
        a3 = input(">").lower()
        
        if a3 == "j":
            
            Writing_animation_Line(19)
            x3 = input("Name: ")
            Schwierigkeit()
            
        
        elif a3 == "n":
            
            x3 = "Rex"
            Schwierigkeit()
            
        
        else:
            
            Writing_animation_Line(2)
            Auswahl(3)   
    
    else:
        
        Writing_animation_Line(3)
        Auswahl(0)   
    
def Schwierigkeit():
    
    Clearscreen()
    Writing_animation_Line(23)
    global attackchance
    global character1HP
    global character1ATK
    global character1DEF
    global character2HP
    global character2ATK
    global character2DEF
    global character3HP
    global character3ATK
    global character3DEF
    global schwierigkeit
    schwierigkeit = input(">").lower()
    
    if schwierigkeit == "einfach":
        
        Writing_animation_Line(24)
        Writing_animation_Line(25)
        character1HP = int(int(cfg["character"]["hp"]) * float(cfg[schwierigkeit]["hpschwierigkeit"]))
        character1ATK = int(int(cfg["character"]["atk"]) * float(cfg[schwierigkeit]["atkschwierigkeit"]))
        character1DEF = int(int(cfg["character"]["def"]) * float(cfg[schwierigkeit]["defschwierigkeit"]))
        character2HP = int(int(cfg["character"]["hp"]) * float(cfg[schwierigkeit]["hpschwierigkeit"]))
        character2ATK = int(int(cfg["character"]["atk"]) * float(cfg[schwierigkeit]["atkschwierigkeit"]))
        character2DEF = int(int(cfg["character"]["def"]) * float(cfg[schwierigkeit]["defschwierigkeit"]))
        character3HP = int(int(cfg["character"]["hp"]) * float(cfg[schwierigkeit]["hpschwierigkeit"]))
        character3ATK = int(int(cfg["character"]["atk"]) * float(cfg[schwierigkeit]["atkschwierigkeit"]))
        character3DEF = int(int(cfg["character"]["def"]) * float(cfg[schwierigkeit]["defschwierigkeit"]))
        attackchance = int(int(cfg[schwierigkeit]["angriffchance"]))
        time.sleep(5)

    elif schwierigkeit == "normal":
        
        Writing_animation_Line(24)
        Writing_animation_Line(26)
        character1HP = int(int(cfg["character"]["hp"]) * float(cfg[schwierigkeit]["hpschwierigkeit"]))
        character1ATK = int(int(cfg["character"]["atk"]) * float(cfg[schwierigkeit]["atkschwierigkeit"]))
        character1DEF = int(int(cfg["character"]["def"]) * float(cfg[schwierigkeit]["defschwierigkeit"]))
        character2HP = int(int(cfg["character"]["hp"]) * float(cfg[schwierigkeit]["hpschwierigkeit"]))
        character2ATK = int(int(cfg["character"]["atk"]) * float(cfg[schwierigkeit]["atkschwierigkeit"]))
        character2DEF = int(int(cfg["character"]["def"]) * float(cfg[schwierigkeit]["defschwierigkeit"]))
        character3HP = int(int(cfg["character"]["hp"]) * float(cfg[schwierigkeit]["hpschwierigkeit"]))
        character3ATK = int(int(cfg["character"]["atk"]) * float(cfg[schwierigkeit]["atkschwierigkeit"]))
        character3DEF = int(int(cfg["character"]["def"]) * float(cfg[schwierigkeit]["defschwierigkeit"]))
        attackchance = int(cfg[schwierigkeit]["angriffchance"])
        time.sleep(5)

    elif schwierigkeit == "schwer":
        
        Writing_animation_Line(24)
        Writing_animation_Line(27)
        character1HP = int(int(cfg["character"]["hp"]) * float(cfg[schwierigkeit]["hpschwierigkeit"]))
        character1ATK = int(int(cfg["character"]["atk"]) * float(cfg[schwierigkeit]["atkschwierigkeit"]))
        character1DEF = int(int(cfg["character"]["def"]) * float(cfg[schwierigkeit]["defschwierigkeit"]))
        character2HP = int(int(cfg["character"]["hp"]) * float(cfg[schwierigkeit]["hpschwierigkeit"]))
        character2ATK = int(int(cfg["character"]["atk"]) * float(cfg[schwierigkeit]["atkschwierigkeit"]))
        character2DEF = int(int(cfg["character"]["def"]) * float(cfg[schwierigkeit]["defschwierigkeit"]))
        character3HP = int(int(cfg["character"]["hp"]) * float(cfg[schwierigkeit]["hpschwierigkeit"]))
        character3ATK = int(int(cfg["character"]["atk"]) * float(cfg[schwierigkeit]["atkschwierigkeit"]))
        character3DEF = int(int(cfg["character"]["def"]) * float(cfg[schwierigkeit]["defschwierigkeit"]))
        attackchance = int(cfg[schwierigkeit]["angriffchance"])
        time.sleep(5)

    else:
        
        Writing_animation_Line(28)
        Schwierigkeit()
    

 #character(spieler,gegner) erstellung


#start des spieles, nachdem mal alles ausgewählt hat.

####################################### GAME MENU ##########################################

def Menu():

    Clearscreen()
    Menu_Screen()
    print("Anmelden")
    print("Optionen")
    menuauswahl = input(">").lower()
    
    if menuauswahl == "anmelden":
        
        Anmelden()
        
    elif menuauswahl == "optionen":
        
        Optionen()
        
    else:
        
        Writing_animation_Line(2)
        Clearscreen()
        Menu()

def Optionen():

    
    while platform.system() != "Windows":

        Writing_animation_Line(48)
        Writing_animation_Line(14)
        input()
        Menu()
    
    Optionen_Screen()
    print("1. Farben ändern")
    print("2. Zurück")
    optionenauswahl = input(">")

    if optionenauswahl == "1":

        Clearscreen()
        Optionen_Screen()
        Writing_animation_Line(49)
        
        for i in fcl.values():
            
            Writing_animation_Print(i + "\n")
        
        fcauswahl = input(">")

        if fcauswahl in fcl.values():
            
            for fcn, cn in fcl.items():
                
                if fcauswahl == cn:
                    
                    fc = fcn
        
        else:

            Writing_animation_Line(2)
            Optionen()

        Clearscreen()
        Optionen_Screen()
        Writing_animation_Line(50)
        
        for i in bcl.values():
            
            Writing_animation_Print(i + "\n")
        
        bcauswahl = input(">")
        
        if bcauswahl in bcl.values():
            
            for bcn, cn in bcl.items():
                
                if bcauswahl == cn:
                    
                    bc = bcn
            
            os.system("color " + str(bc) + fc)
            Menu()
        
        else:

            Writing_animation_Line(2)
            Optionen()

    elif optionenauswahl == "2":

        Menu()
        
    else:
        
       Writing_animation_Line(2)
       Optionen()

def Anmelden():

    Jsonfile_Loading()
    Clearscreen()
    Login()
    Auswahl(0)
    Loading()
    Story()
    Start()

def End_Screen(ende):

    print("#" * (os.get_terminal_size().columns -2))
    Writing_animation_Print("# Dein Spielmodus: " + schwierigkeit)
    Writing_animation_Print("# Besuchte Ein-/Ausgänge: " + len(beag) + "/" + len(ag+eg))
    Writing_animation_Print("# Besuchte Sackgassen: " + len(bsg) + "/" + len(sg))
    Writing_animation_Print("# Gefundene Items: " + len(spieler.inventory) + "/" + len(itemlist))
    Writing_animation_Print("# Cheatcode benutzt: " + str(cheatcode))
    print("#" * (os.get_terminal_size().columns -2))

############################## GAME START ######################################


def Story():

    Clearscreen()
    Title("Vorgeschichte")
    Writing_animation_Line(54)
    Writing_animation_Line(55)
    Writing_animation_Line(56)
    Writing_animation_Line(57)
    Writing_animation_Line(58)
    Writing_animation_Line(59)
    Writing_animation_Line(60)
    Writing_animation_Line(61)
    Writing_animation_Line(62)
    Writing_animation_Line(63)
    Writing_animation_Line(64)
    Writing_animation_Line(65)
    Writing_animation_Line(66)
    Writing_animation_Line(67)
    Writing_animation_Line(68)
    Writing_animation_Line(14)
    input()


def Start():
    
    Title(titlename)
    Position()


def Loading():
      
    Title("Ladebildschirm")
    Clearscreen()
    Item_Loading(sg)
    Inventory_Loading()
    Character_Loading()
    Loading_Screen("Map", len(map))
    Writing_animation_Line(14)
    input()


def Main():
    
    bc = 0
    fc = "f"
    os.system("color " + str(bc) + fc)
    Menu()
    


    

####################################### MENÜ #################################



Menu()
