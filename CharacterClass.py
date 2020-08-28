from Essentials import Writing_animation_Line
from Essentials import Writing_animation_Print


class Character():
    
    #Attribute des Monsters werden im mKonstruktor festgelegt
    def __init__(self, name, HP, ATK, DEF, position, inventory):
        
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.position = position
        self.inventory = inventory 
    
    #Methoden
    def Angreifen(self, gegner):
        
        if (int(gegner.DEF) < int(self.ATK)):
            
            #Du hast mehr ATK als gegner DEF
            Writing_animation_Print(gegner.name + " erleidet Schaden.\n")
            gegner.HP = int(gegner.HP) - (int(self.ATK) - int(gegner.DEF))
            Writing_animation_Print(gegner.name + " hat nur noch " + str(gegner.HP) + " HP \n")
        
        elif (int(gegner.DEF) > int(self.ATK)):
            
            #Du hast weniger ATK als gegner DEF
            Writing_animation_Print(self.name + " erleidet Schaden.\n")
            self.HP = int(self.HP) - (int(gegner.DEF) - int(self.ATK))
            Writing_animation_Print(self.name + " hat nur noch " + str(self.HP) + " HP \n")
        
        elif (int(gegner.DEF) == int(self.ATK)):
            
            #Du machst kein Schaden
            Writing_animation_Line(37)

    def AddItem(self, item):

        self.HP = int(self.HP) + int(item.HP)
        self.ATK = int(self.ATK) + int(item.HP)
        self.DEF = int(self.DEF) + int(item.DEF)
        Writing_animation_Print(item.name + " ist jetzt in deinem Inventar. \n")
            