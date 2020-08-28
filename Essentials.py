#!/usr/bin/env python
# -*- coding: utf-8 -*-


from random import uniform
from time import sleep
import platform
import codecs
import uuid 
import sys
import os


usernumber = "Unit" + str(int((float(uuid.uuid4().int)*10/float(uuid.uuid4().int))+1))
userpw = "0"
system = platform.system()
fcl = {"a": "Hellgrün", "b": "Helltürkis", "c": "Hellrot", "d": "Helllila", "e": "Hellgelb", "f": "Weiß"}
bcl = {0:"Schwarz",1: "Blau", 2: "Grün", 3: "Türkis", 4: "Rot", 5: "Lila", 6: "Gelb", 7: "Hellgrau", 8: "Grau", 9: "Hellblau"}

#essentials für das Spiel
#unnötig aber toll
#funktioniert aber noch nicht :(
#update: 11.02.2020: writinganimation funktioniert yay



def Writing_animation_Line(l):                                        
    
    with codecs.open("story.txt" , "r", "utf-8", "strict") as text:
    
        for a, line in enumerate(text,1):
                                           
            if a == l:                                                                                                                     
                
                for char in line:                                          
                    
                    sys.stdout.write(char)
                    sys.stdout.flush()                                   
                    sleep(uniform(0,0.05))                             


def Writing_animation_Print(text):
    
    for char in text:
        
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(uniform(0,0.05))
  
def Clearscreen():
    
    if system == "Windows":
        
        os.system("cls")
        
    else:
        
        os.system("reset")

def Title(title):
    
    if system == "Windows":
        
        os.system("title " + title)
        os.system("mode 112,30")
        
    else:

        sys.stdout.write("\x1b]2;" + title + "\x07")
        os.system("printf '\e[8;30;112t'")


def Login():
    
    Title("Benutzernummer: " + str(usernumber) + "; Benutzerpasswort: " + str(userpw))
    Clearscreen()
    Writing_animation_Line(7)
    login = input("Benutzernummer: ")
    passwd = input("Passwort: ")
    
    while usernumber != login or str(userpw) != passwd:
        
        Clearscreen()
        Writing_animation_Line(8)
        Writing_animation_Line(9)
        login = input("Benutzernummer: ")
        passwd = input("Passwort: ")    
    
    Writing_animation_Line(10)
        
def ASCII_pic(pic):

    Clearscreen()
    
    with codecs.open(pic,"r","utf-16be","strict") as picture:
    
        for line in picture:
            
            print(line.rstrip())
    
    print("\n" * 3)


def Loading_Screen(name,end):
    
    for i in range(int(end)):

        sleep(uniform(0.05,0.1))
        sys.stdout.write("\r" + name + ": " + str(i) + "/" + str(end) + " geladen.")
        sys.stdout.flush()
    
    sys.stdout.write("\r" + name + ": " + str(end) + "/" + str(end) + " fertig geladen. \n")


def Optionen_Screen():

    Title("Optionen")
    optionen = ".: Optionen :."
    breite = os.get_terminal_size().columns - 2
    abstandoptionen = ((int(breite) - int(2))/int(2)) - int(len(optionen))/int(2)
    print("#" * breite)
    print("#" + " " * int(abstandoptionen) + optionen + " " * int(abstandoptionen) + "#")
    print("#" * breite + "\n" * 3)

def Menu_Screen():

    Title("Launcher")
    ASCII_pic("logo.txt")
    