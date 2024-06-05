#imports
import random
#Lists
GuardNotCaptured = []
PeasentNotCaptured = []
GuardsCaptured = []
PeasentsCaptured = []
MonarchAlive = []
PeasentAlive = []
GuardAlive = []
Choice1 = ["attack", "capture"]
Choice2 = ["attack", "execute", "capture"]
executioners = []
Catchphrases = [" tries to scurry away", " yells for help", " attempts to fight back", " orders you to go away", "i gave you cake!"]
PeasentsCanBeCaptured = []


#define classses
class People:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(100, 501)
        self.alive = True
    
        
class Fighters(People):
    def __init__(self, name):
        super().__init__(name)
        self.strength = random.randint(10,51)
        self.captured = False
            
        
    def __str__(self):
        return self.name + " is a "+ type(self).__name__+ ". Their health is "+ str(self.health) + ". Their Strength is " +str(self.strength)+"."

    def capture(self, target):
        if self.captured == True:
            print("You cant do anything while your captured!")
        elif self.alive == False:
            print("You cant do anything if your dead!")
        else:
            target.getCaptured()
        
class Peasent(Fighters):
    def __init__(self, name):
        super().__init__(name)
        PeasentAlive.append(self)
        PeasentNotCaptured.append(self)
        print(self, self.name, "can riot to attack a guard or capture guards when their health drops below 100!")
        
    def hurt(self, HP):
        if not self.alive:
            print(self.name," is already dead! You cant attack them.")
        elif self.health <= HP:
            print(self.name, "has died!")
            self.alive = False
            self.captured = True
            PeasentAlive.remove(self)
            if self in PeasentNotCaptured == True:
                PeasentNotCaptured.remove(self)
            if self in PeasentsCaptured == True:
                PeasentsCaptured.remove(self)
            if self in PeasentsCanBeCaptured == True:
                PeasentsCanBeCaptured.remove(self)
            if len(PeasentAlive) == 0:
                print("All of the peasents died. You Lost :(")
                exit(0)
        else: 
            self.health -= HP
            print(self.name +  " has" ,self.health, "HP left.")
        if self.health < 100:
            PeasentsCanBeCaptured.append(self)
    
    def getCaptured(self):
        if self.name in PeasentAlive == False:
            print(self.name," is already dead! You cant capture them.")
        elif self.captured == True:
            print(self.name, "has already been captured.")
        elif self.health > 100:
            print("You can only capture people onec thier health is below 100!")
        else:
            print(self.name, "has been captured")
            PeasentsCaptured.append(self)
            PeasentNotCaptured.remove(self)
            PeasentsCanBeCaptured.remove(self)
            self.captured = True
            if len(PeasentNotCaptured) == 0:
                print("All the Peasents are captured! You Lose :(")
                exit(0)

    def heal(self, HP):
        if not self.alive:
            print(self.name," is already dead! You cant heal them.")
        else:
            self.health += HP
            print(self.name + " has been healed and has" ,self.health, "HP left")

    def revive(self):
        if self.alive:
            print(self.name, "is alive! You cant revive them!")
        else:
            PeasentAlive.append(self)
            self.health = 50
            print(self.name, "has been revived!")
        
    def riot(self, target): 
        if self.captured == True:
            print("You cant do anything while your captured!")
        elif self.alive == False:
            print("You cant do anything if your dead!")
        else:
            print(self.name, "attacks", target.name +"!")
            target.hurt(self.strength)
        Guard.GuardsTurn()

           
    
    
class Guard(Fighters):
    def __init__(self, name):
        super().__init__(name)
        GuardAlive.append(self)
        GuardNotCaptured.append(self)
        
    def hurt(self, HP):
        if not self.alive:
            print(self.name," is already dead! You cant attack them.")
        elif self.health <= HP:
            print(self.name, "has died!")
            self.alive = False
            GuardAlive.remove(self)
            GuardNotCaptured.remove(self)
            if len(GuardAlive) == 0:
                print("All of the Guards died. You can now kill the monarch!")
                
        else: 
            self.health -= HP
            print(self.name +  " has" ,self.health, "HP left.")
    
    def getCaptured(self):
        if self.alive == False:
            print(self.name," is already dead! You cant capture them.")
        elif self.captured == True:
            print(self.name, "has already been captured.")
        elif self.health > 100:
            print("You can only capture people onec thier health is below 100!") 
        else:
            print(self.name, "has been captured")
            GuardsCaptured.append(self)
            GuardNotCaptured.remove(self)
            GuardAlive.remove(self)
            self.captured = True
            if len(GuardNotCaptured) == 0:
                print("All the guards are captured! You can now kill the monarch!")
    def attack(self, target):
                    target.hurt(self.strength)
            
    def GuardsTurn():
        if len(GuardAlive) == 0 or len(GuardNotCaptured) == 0:
            pass
        else:
            print("------- ENEMYS TURN -------")
            if len(PeasentsCaptured) > 0:
                choice = random.choice(Choice2)
                if choice == "attack":
                    guard = random.choice(GuardNotCaptured)
                    target = random.choice(PeasentNotCaptured)
                    print(guard.name, "attacks", target.name+"!")
                    guard.attack(target)
                elif choice == "capture":
                    if len(PeasentsCanBeCaptured) > 0:
                        guard = random.choice(GuardNotCaptured)
                        target = random.choice(PeasentsCanBeCaptured)
                        guard.capture(target)
                    else:
                        guard = random.choice(GuardNotCaptured)
                        target = random.choice(PeasentNotCaptured)
                        print(guard.name, "attacks", target.name+"!")
                        guard.attack(target)
                elif choice == "execute":
                    executer = random.choice(executioners)
                    target = random.choice(PeasentsCaptured)
                    print(executer.name, "has executed", target.name+"!")
                    PeasentsCaptured.remove(target)
                    if target in PeasentsCanBeCaptured == True:
                        PeasentsCanBeCaptured.remove(target)
                    Executioner.execute(executer, target)
            elif len(PeasentsCanBeCaptured) > 0:
                choice = random.choice(Choice1)
                if choice == "attack":
                    guard = random.choice(GuardNotCaptured)
                    target = random.choice(PeasentNotCaptured)
                    print(guard.name, "attacks", target.name+"!")
                    guard.attack(target)
                elif choice == "capture":
                    guard = random.choice(GuardNotCaptured)
                    target = random.choice(PeasentsCanBeCaptured)
                    guard.capture(target)
                    
            else:
                guard = random.choice(GuardNotCaptured)
                target = random.choice(PeasentNotCaptured)
                print(guard.name, "attacks", target.name+"!")
                guard.attack(target)
                
            print("------- YOUR TURN -------")

class Assassin(Fighters):
    def __init__(self, name):
        super().__init__(name)
        self.strength = 1000
    
    def assassinate(self, target):
        self.chance = random.randint(1,50)
        if self.chance == 50:
            target.assassignated(self.strength)
            print(target, " was assasinated")
        else:
            print('Assasination unsuccsessful')
        

class Healer(People):
    def __init__(self, name):
        super().__init__(name)
        self.power = random.randint(1, 100)

    def heal(self, target):
        hit = random.randint(1,21)
        if hit >= 5:
            target.heal(self.power)

    


class Necromancer(People):
    def __init__(self, name):
        super().__init__(name)

    def revive(self, target):
        target.revive()



    
class Monarch(People):
    def __init__(self, name):
        super().__init__(name)
        MonarchAlive.append(self)
    def __str__(self):
        return self.name + " is a "+ type(self).__name__
    
    def hurt(self, HP):
        if not self.alive:
            print(self.name," is already dead! You cant attack them.")
        elif len(GuardNotCaptured) > 0:
            print("You cant get to the monarch! Their protected by guards!")
        elif len(GuardAlive) > 0:
            print("You cant get to the monarch! Their protected by guards!")
        elif self.health <= HP:
            print("You killed ",self.name,"!")
            self.alive = False
            MonarchAlive.remove(self)
            if len(MonarchAlive) == 0:
                print("You killed the Monarchs and won the game!")
                exit(0)
        else: 
            self.health -= HP
            print("You delt " + str(HP) +" HP of damage!")
            print(self.name, "is still alive")
            print("------- MONARCHS TURN -------")
            print(self.name + random.choice(Catchphrases))
            print("------- YOUR TURN -------")
    def assassignated(self, HP):
            if not self.alive:
                print(self.name," is already dead! You cant kill them.")
            elif self.health <= HP:
                print("You killed ",self.name,"!")
                self.alive = False
                MonarchAlive.remove(self)
                if len(MonarchAlive) == 0:
                    print("You killed the Monarchs and won the game!")
                    exit(0)
            else:
                self.health -= HP
                print("You killed", self.name,"!")


class Executioner:
    def __init__(self, name):
        self.name = name
        self.strength = 1000
        executioners.append(self)
    def __str__(self):
        return self.name + " is a "+ type(self).__name__
    
    def execute(self, target):
        target.hurt(self.strength)
        
    
#functions

#main
print('''Welcome to The French Revolution Game!"
"Here's how to play!
    - First create the Monarchs, Guards, and Executioners Having many charecters is best but just
  have at least 1 of each!
     sample syntax: 
       queen = Monarch("queen")
       ben = Guard("ben")
       jeff = Executioner("jeff")
    - Next create the Peasents, assassins, Healers, and Necromancers! This is who you play as!
        sample syntax:
           fred = Peasent("fred")
           allen = Assassin("allen")
           ted = Healer("ted")
           buddy = Necromancer("buddy")
    - Then start the revolution by telling your peasents to riot!
        sample syntax:
           fred.riot(ben)
    - Your assassins can a 1 in 50 chance of killing anyone imeditaly inclding a monarch, even if all the guards arnt dead yet!
    - Healers heal your peasents up to 100 HP
    - Necromancers have a 1 in 30 chance of reviving one of your peasents
    - After that keep fighting until you kill the monarch and win the game!
Have fun! 
Optional setup:
queen = Monarch("queen")
ben = Guard("ben")
joe = Guard("joe")
billy = Guard("billy")
jeff = Executioner("jeff")
fred = Peasent("fred")
bob = Peasent("bob")
allen = Assassin("allen")
ted = Healer("ted")
buddy = Necromancer("buddy") 
''')

