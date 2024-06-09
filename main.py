#Import Packages
from os import system, name
import time
import pyinputplus as pyip
import random
import sys
from art import *

#Assigning global variables
Avengers = ['Black Panther', 'Thor', 'Spiderman', 'Hawkeye', 'Dr. Strange', 'Antman'] #Heros you can use in the game
played_Avengers = [] #This list will contain heros you have already played
stones = ['Space Stone', 'Reality Stone', 'Power Stone', 'Mind Stone', 'Time Stone', 'Soul Stone'] #Stones left to collect
coins = 100 #Player's Coins
health = 100 #Player's Health
gauntlet = False #Identifier for infinity gauntlet
infinity_gauntlet = [] #List for collected stones
king_eitri_met = False #Identifier to show if you have met King Eitre
tprint("WHAT IF \nYOU SAVED \nTHE UNIVERSE?")
name = pyip.inputStr("Please type your name:\n") #Asks for player's name
location = "Home" #Current location

#How to clear screen in python? (2018, April 1). GeeksforGeeks. https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    """
    Clears Screen
    """
    #For Windows
    if name == 'nt':
        _ = system('cls')
    #For Mac and Linux
    else:
        _ = system('clear')
        
def enter():
    """
    Asks player to enter before continuing to next stage.
    """
    input("Press enter to continue.\n")
    
def status():
    """
    Shows current status of the game.
    """
    global coins
    global health
    global infinity_gauntlet
    global gauntlet
    global location
    
    print(f"Coins: {coins}")
    print(f"Health: {health}%")
    print(f"Location : {location}")
    #Checks if player has obtained the Infinity Gauntlet
    if gauntlet == True:
        print(f"Infinity Gauntlet: Obtained")
        print(f"Infinity Stones: {infinity_gauntlet}")
    else:
        print(f"Infinity Gauntlet: Missing")
    print("===========================================================")
    
def intro():
    """
    Introduction to the game story.
    """
    global Avengers
    global name
    status()
    print("You are having dinner with your family and, suddenly everyone around you turned to dust.")
    time.sleep(0.5)
    print("You start to panic as you have no idea what is happening.")
    time.sleep(0.5)
    print("A sparkling light start to appear behind you.")
    time.sleep(0.5)
    print("You turn around and see a portal of some kind.")
    time.sleep(0.5)
    print(f"From the portal, Dr. Strange came out and said {name.title()}, you are our only hope to save humanity.")
    enter()
    clear()
    status()
    print(f"You asked without hesitation, how can I help?")
    time.sleep(0.5)
    print("He started to explain what has happened.")
    time.sleep(0.5)
    print("Dr. Strange: Thanos has wiped out half of all living creatures.")
    time.sleep(0.5)
    print("Dr. Strange: Thor managed to kill Thanos but not before he used the infinity stones.")
    time.sleep(0.5)
    print("Dr. Strange: After the deed was done, some of the villians took the infinity stones.")
    time.sleep(0.5)
    print("Dr. Strange: I happens to be one of the survivor of this crisis.")
    time.sleep(0.5)
    print("Dr. Strange: Just before I gave the time stone to Thanos, I looked through 14,000,000 possible outcome where the huminity survives.")
    time.sleep(0.5)
    print(f"{name.title()}: And?")
    time.sleep(0.5)
    print("Dr. Strange: And, there was only one where humanity survives.")
    time.sleep(0.5)
    print(f"Dr. Strange: In the reality where you, {name.title()} lead the Avengers and revive humanity.")
    time.sleep(0.5)
    enter()
    clear()
    status()
    print(f"{name.title()}: Who are the Avengers that survived?")
    time.sleep(0.5)
    print(f"Dr. Strange: The Avengers who survived are,")
    for avenger in Avengers:
        print(avenger)
    enter()
    clear()
    status()
    print('Dr. Strange: Now its up to you to lead us and save humanity.')
    time.sleep(0.5)
    print("Dr. Strange: Remember every Avengers have their roles to play including mine.")
    time.sleep(0.5)
    print("Dr. Strange: I can only give you advice about who has the infinity stone but how to retrive them, is going to be your job.")
    time.sleep(0.5)
    print("Dr. Strange: You can choose each avenger to retrive a infinity stone, only once.")
    time.sleep(0.5)
    print("Dr. Strange: And here are hundred gold coins, you can use them however you may like.")
    time.sleep(0.5)
    print("Dr. Strange: I will always be here, in your house, if you need me.")
    time.sleep(0.5)
    enter()
    clear()
    
def eat():
    """
    Action to restore health
    """
    global coins
    global health
    status()
    print("It will cost you 5 gold coins to eat but will increase your health by 20%. Do you want to continue (y/n)?")
    y_n = pyip.inputYesNo()
    if y_n == 'yes' and coins >= 5: #Checks if input is yes and player has atleast 5 coins
        coins -= 5
        if health >= 80:
            health = 100
        else:
            health += 20
        time.sleep(0.5)
        print("You paid 5 gold coins.")
        time.sleep(0.5)
        print(f"Your health is {health}%")
        enter()
        clear()
        free_roam()
    elif y_n == 'yes' and coins < 5:
        print("Sorry you don't have enough coins.")
        time.sleep(0.5)
        enter()
        clear()
        free_roam()
    else: #if player inputs no
        enter()
        clear()
        free_roam()

def rock_paper_scissors():
    """
    Returns result of rock paper scissors game
    """
    choice = pyip.inputMenu(['rock', 'paper', 'scissors'], lettered=False, numbered=True) #Player's choice
    drs_choice = random.choice(['rock', 'paper', 'scissors']) #Dr. Strange's choice
    if (choice == 'rock' and drs_choice == 'paper') or (choice == 'paper' and drs_choice == 'scissors') or (choice == 'scissors' and drs_choice == 'rock'):
        result = 'lose'
    elif (choice == 'paper' and drs_choice == 'rock') or (choice == 'scissors' and drs_choice == 'paper') or (choice == 'rock' and drs_choice == 'scissors'):
        result = 'win'
    else:
        result = 'draw'
    return result

def game():
    """
    Player plays rock paper scissors with Dr. Strange
    player can earn money from this game
    """
    global name
    global coins
    status()
    print('You ask Dr. Strange to play rock paper scissors with you. He agrees.')
    time.sleep(0.5)
    print("To make the game he says let's play with gold coins.")
    time.sleep(0.5)
    print('If you win or, make a draw you get 10 gold coins and, if you lose, you give me 10 gold coins.')
    time.sleep(0.5)
    print('Do you want to play (y/n)?')
    y_n = pyip.inputYesNo()
    if y_n == 'yes' and coins >= 10:
        result = rock_paper_scissors()
        if result == 'win':
            print('You win. Dr. strange gave you 10 gold coins.')
            coins += 10
        elif result == 'draw':
            print("It's a draw. Dr. strange gave you 10 gold coins.")
            coins += 10
        else:
            print("You lose. You gave Dr. Strange 10 gold coins")
            coins -= 10
        enter()
        clear()
        free_roam()
    elif y_n == 'yes' and coins <10:
        #If player has less than 10 coins. Dr. Strange gives 30 coin to player
        print("You say that you don't have any coins to play with. Dr. Strange gives you 30 coins.")
        coins += 30
        enter()
        clear()
        free_roam()
    else:
        enter()
        clear()
        free_roam()    

def nidavellir():
    """
    This is the room where you get the Infinity Gauntlet.
    """
    global name
    global king_eitri_met
    global coins
    global gauntlet
    global location
    location = 'Nidavellir'
    if king_eitri_met == False:
        #If you are meeting King Eitri for the first time
        status()
        print("You suddenly entered place that looked like a battle field with dead bodies laying all over the place.")
        time.sleep(0.5)
        print("Suddenly a dwarf begins to run towards you with an axe in his hand.")
        time.sleep(0.5)
        print("Dwarf: THANOS!!!")
        time.sleep(0.5)
        print("You not knowing what to do, begin to run away.")
        time.sleep(0.5)
        print(f"{name.title()}: I AM NOT THANOS. I AM {name.upper()}!!!")
        time.sleep(0.5)
        print("You both stopped running and begin to calm down.")
        time.sleep(0.5)
        enter()
        clear()
        status()
        print(f"{name.title()}: Who are you? And what happened here?")
        time.sleep(0.5)
        print("Dwarf: I am King Eitri. And Thanos happened.")
        time.sleep(0.5)
        print("King Eitri: Thanos came and, asked us to make him an infinity guntlet. When we refused, he begin killing every one.")
        time.sleep(0.5)
        print("King Eitri: We were powerless against him. So, we gave in and, created an infinity guntlet for him.")
        time.sleep(0.5)
        print("King Eitri: But even after we gave him the guntlet, he killed everyone anyway.")
        time.sleep(0.5)
        print("King Eitri: I am not sure why only I was left alive.")
        time.sleep(0.5)
        print(f"{name.title()}: Hi, I am {name.title()}.")
        time.sleep(0.5)
        print(f"{name.title()}: I think you being alive and, we meeting here was destiny.")
        time.sleep(0.5)
        print(f"King Eitri: What do you mean?")
        time.sleep(0.5)
        print(f"{name.title()}: I am on a mission to save humanity and, undo what Thanos did to us.")
        time.sleep(0.5)
        print(f"King Eitri: And how are you going to do that?")
        time.sleep(0.5)
        print(f"{name.title()}: I am going to collect all the infinity stones and, revive all those Thanos killed.")
        time.sleep(0.5)
        print(f"King Eitri: HAHAHAHA, Good Luck doing that!")
        time.sleep(0.5)
        print(f"{name.title()}: Hey, don't laugh. I am serious.")
        time.sleep(0.5)
        print(f"King Eitri: Seriously?")
        time.sleep(0.5)
        print(f"{name.title()}: Yes, but before I do that I need you to make me an infinity gauntlet.")
        time.sleep(0.5)
        print(f"King Eitri: Sorry, can't do that.")
        time.sleep(0.5)
        print(f"{name.title()}: Why?")
        time.sleep(0.5)
        print(f"King Eitri: Thanos took all the gold we had. And can't make it without any gold.")
        time.sleep(0.5)
        print(f"{name.title()}: Will gold coins work?")
        time.sleep(0.5)
        print(f"King Eitri: Yes it will.")
        time.sleep(0.5)
        enter()
        clear()
        status()
        print(f"{name.title()}: How many gold coins do you need?")
        time.sleep(0.5)
        print(f"King Eitri: 50 gold coins should be enough. Do you have 50 gold coins (y/n)?")
        time.sleep(0.5)
        y_n = pyip.inputYesNo()
        if coins >= 50 and y_n == 'yes':
            #If you have 50 coins
            time.sleep(0.5)
            print(f"{name.title()}: Here is 50 coins.")
            coins -= 50
            time.sleep(0.5)
            print("King Eitri made you a gautlet. You thanked him and, returned home through the portal.")
            gauntlet = True
            enter()
            clear()
            free_roam()
        else:
            time.sleep(0.5)
            print(f"{name.title()}: Sorry, I don't have that many gold right now. I will be back with more gold next time.")
            time.sleep(0.5)
            print(f"You went back home with out gauntlet.")
            enter()
            clear()
            free_roam()
    elif king_eitri_met == True:
        #If you already met King Eitri
        status()
        print(f"{name.title()}: Hi, I am back.")
        time.sleep(0.5)
        print("King Eitri: Do you have 50 gold coins (y/n)?")
        time.sleep(0.5)
        y_n = pyip.inputYesNo()
        if coins >= 50 and y_n == 'yes':
            #Checks if you have 50 coins
            print(f"{name.title()}: Here is 50 coins.")
            time.sleep(0.5)
            coins -= 50
            print("King Eitri made you a gautlet. You thanked him and returned home through the portal.")
            time.sleep(0.5)
            gauntlet = True
            enter()
            clear()
            free_roam()
        else:
            print(f"{name.title()}: Sorry, I don't have that many gold right now. I will be back with more gold next time.")
            time.sleep(0.5)
            print(f"You went back home with out gauntlet.")
            enter()
            clear()
            free_roam()

def tesseract(partner):
    """
    This room is where you collect the Space Stone.
    """
    global location
    global name
    global coin
    global health
    global infinity_gauntlet
    global stones
    location = 'Wakanda'
    status()
    print("You reach Wakanda and, Kilmongor is right in front of you.")
    time.sleep(0.5)
    print(f"Kilmongor and, {partner} begin to fight as soon as their eyes met.")
    time.sleep(0.5)
    if partner == 'Hawkeye': #If partner is Hawkeye
        health -= 60
        print(f"You got injured and, your health is at {health}%")
        if health <= 0:
            health = 0
            print("You died.")
            time.sleep(0.5)
            tprint("GAME OVER")
            time.sleep(0.5)
            sys.exit('Thank you for playing.')
        else:
            print(f"After a hard fought battle you and, {partner} won the battle and, retrive the Space Stone.")
            time.sleep(0.5)
            stones.remove('Space Stone')
            infinity_gauntlet.append('Space Stone')
            print("You returned home using the Space Stone.")
            time.sleep(0.5)
            enter()
            clear()
            free_roam()        
    elif partner == 'Black Panther' or partner == 'Antman': #If partner is Black Panther or Antman
        health -= 40
        print(f"You got injured and your health is at {health}%")
        if health <= 0:
            health = 0
            print("You died.")
            time.sleep(0.5)
            tprint("GAME OVER")
            time.sleep(0.5)
            sys.exit('Thank you for playing.')
        else:
            print(f"After a hard fought battle you and, {partner} won the battle and, retrive the Space Stone.")
            time.sleep(0.5)
            stones.remove('Space Stone')
            infinity_gauntlet.append('Space Stone')
            print("You returned home using the Space Stone.")
            time.sleep(0.5)
            enter()
            clear()
            free_roam()
    elif partner == 'Spiderman': #If your partner is Spiderman
        health -= 20
        print(f"You got injured and, your health is at {health}%")
        if health <= 0:
            health = 0
            print("You died.")
            time.sleep(0.5)
            tprint("GAME OVER")
            time.sleep(0.5)
            sys.exit('Thank you for playing.')
        else:
            print(f"It was an easy battle. You and, {partner} won the battle and, retrive the Space Stone.")
            time.sleep(0.5)
            stones.remove('Space Stone')
            infinity_gauntlet.append('Space Stone')
            print("You returned home using the Space Stone.")
            time.sleep(0.5)
            enter()
            clear()
            free_roam()
    else:
        print(f"{partner} was too over powered for Killmongor. You won before the battle began.")
        time.sleep(0.5)
        stones.remove('Space Stone')
        infinity_gauntlet.append('Space Stone')
        print("You returned home using the Space Stone.")
        time.sleep(0.5)
        enter()
        clear()
        free_roam()

def aether():
    """
    The room where you retrieve the Reality Stone.
    """
    global Avengers
    global played_Avengers
    global name
    global health
    global infinity_gauntlet
    global location
    global stones
    location = "Asgard"
    status()
    print("Dr. Strange: Reality Stone is in the hands of Loki, the God of Mischief.")
    time.sleep(0.5)
    print("Dr. Strange: Choose your avenger wisely, as Loki uses magic.")
    time.sleep(0.5)
    partner = pyip.inputMenu(Avengers, lettered=False, numbered=True)
    print("You use Space Stone to teleport where Loki is.")
    time.sleep(0.5)
    print(f"You and, {partner} suddenly teleport to a beauiful golden city.")
    time.sleep(0.5)
    print("Loki: Welcome to Asgard. I, king of Asgaud welcomes you.")
    time.sleep(0.5)
    print(f"{name.title()}: Loki, give us the stone.")
    time.sleep(0.5)
    print(f"Loki: Try and take it, if you can.")
    time.sleep(0.5)
    print(f"You and, {partner} started to fight Loki")
    time.sleep(0.5)
    if partner == "Thor" or partner == "Dr. Strange": #if partner is Thor or Dr. Strange
        health -= 20
        print(f"You got injured and, your health is at {health}%")
        Avengers.remove(partner)
        played_Avengers.append(partner)
        if health <= 0:
            health = 0
            print("You died.")
            time.sleep(0.5)
            tprint("GAME OVER")
            time.sleep(0.5)
            sys.exit('Thank you for playing.')
        else:
            print("After a long and, magical fight, you won.")
            time.sleep(0.5)
            stones.remove('Reality Stone')
            infinity_gauntlet.append('Reality Stone')
            print("You returned home using the Space Stone.")
            time.sleep(0.5)
            enter()
            clear()
            free_roam() 
    else:
        health = 10
        print(f"You got injured and, your health is at {health}%")
        print(f"You and, {partner} were no match for Loki's magic.")
        time.sleep(0.5)
        print(f"You were losing the fight")
        time.sleep(0.5)
        print(f"You tried to use an infinity stone out of desperation.")
        time.sleep(0.5)
        use_stone = random.choice(infinity_gauntlet)
        enter()
        clear()
        use_gauntlet(use_stone, partner, "Reality Stone")

def power():
    """
    This room is where you retrieve the Power Stone.
    """
    global Avengers
    global played_Avengers
    global name
    global health
    global infinity_gauntlet
    global location
    global stones
    location = "Klyntar"
    status()
    print("Dr. Strange: Power Stone is in taken by Venom symbiote.")
    time.sleep(0.5)
    print("Dr. Strange: Choose your avenger wisely, as Venom is very strong.")
    time.sleep(0.5)
    partner = pyip.inputMenu(Avengers, lettered=False, numbered=True)
    print("You use Space Stone to teleport where Venom is.")
    time.sleep(0.5)
    print(f"You and, {partner} suddenly teleport to a planet.")
    time.sleep(0.5)
    print("You thought to yourself, if you were in hell.")
    time.sleep(0.5)
    print("Venom suddenly attacked you out of know where.")
    time.sleep(0.5)
    health -= 30
    print(f"You got injured and your health is at {health}%")
    if health <= 0:
        health = 0
        print("You died.")
        time.sleep(0.5)
        tprint("GAME OVER")
        time.sleep(0.5)
        sys.exit('Thank you for playing.')    
    if partner == "Thor" or partner == "Dr. Strange": #If your partner is Thor or Dr. Strange
        Avengers.remove(partner)
        played_Avengers.append(partner)
        print("You easily won. He was no match for you.")
        time.sleep(0.5)
        print("You returned home using the Space Stone.")
        stones.remove('Power Stone')
        infinity_gauntlet.append('Power Stone')
        time.sleep(0.5)
        enter()
        clear()
        free_roam()
    elif partner == "Spiderman": #If your partner is Spiderman
        health -= 20
        print(f"You got injured and, your health is at {health}%")
        Avengers.remove(partner)
        played_Avengers.append(partner)
        if health <= 0:
            health = 0
            print("You died.")
            time.sleep(0.5)
            tprint("GAME OVER")
            time.sleep(0.5)
            sys.exit('Thank you for playing.')
        else:
            print("After a long and, tedious fight, you won.")
            time.sleep(0.5)
            stones.remove('Power Stone')
            infinity_gauntlet.append('Power Stone')
            print("You returned home using the Space Stone.")
            time.sleep(0.5)
            enter()
            clear()
            free_roam() 
    else:
        health = 10
        print(f"You got injured and, your health is at {health}%")
        print(f"You and, {partner} were no match for Venom's strength.")
        time.sleep(0.5)
        print(f"You were losing the fight.")
        time.sleep(0.5)
        print(f"You tried to use an infinity stone out of desperation.")
        time.sleep(0.5)
        use_stone = random.choice(infinity_gauntlet)
        enter()
        clear()
        use_gauntlet(use_stone, partner, "Power Stone")        
    
def mind():
    """
    This room has the Mind Stone.
    """
    global Avengers
    global played_Avengers
    global name
    global health
    global infinity_gauntlet
    global location
    global stones
    location = "Outer Space"
    status()
    print("Dr. Strange: Mind Stone is in taken by Ultron.")
    time.sleep(0.5)
    print("Dr. Strange: Be careful. He is currently in space.")
    time.sleep(0.5)
    print("Dr. Strange: If you don't have reality stone, you won't be able to breath in space.")
    time.sleep(0.5)
    print("Dr. Strange: Do you want to go on this mission (y/n)?")
    time.sleep(0.5)
    y_n = pyip.inputYesNo()
    if y_n == 'no':
        print("You decided not to go on this mission.")
        time.sleep(0.5)
        enter()
        clear()
        free_roam()
    else:
        print("Dr. Strange: Be careful. Ultron is an AI. Only a god or, an electronic engineer will be able to win against him.")
        time.sleep(0.5)
        partner = pyip.inputMenu(Avengers, lettered=False, numbered=True)
        print("You use Space Stone to teleport where Ultron is.")
        time.sleep(0.5)
        print(f"You and, {partner} suddenly teleport to a dark space.")
        time.sleep(0.5)
        print("Nothing could be seen anywhere.")
        time.sleep(0.5)
        print("Only one being was there, it was Ultron.")
        time.sleep(0.5)
        print("You started to fight.")
        time.sleep(0.5)
        if "Reality Stone" in infinity_gauntlet: #Checks if you have the Reality Stone
            if partner == "Thor": #If partner is thor
                Avengers.remove(partner)
                played_Avengers.append(partner)
                health -= 50
                print(f"You got injured and, your health is at {health}%")
                if health <= 0:
                    health = 0
                    print("You died.")
                    time.sleep(0.5)
                    tprint("GAME OVER")
                    time.sleep(0.5)
                    sys.exit('Thank you for playing.')
                else:
                    print("It was a hard fight but you some how won.")
                    time.sleep(0.5)
                    stones.remove('Mind Stone')
                    infinity_gauntlet.append('Mind Stone')
                    print("You returned home using the Space Stone.")
                    time.sleep(0.5)
                    enter()
                    clear()
                    free_roam() 
            elif partner == "Antman": #If partner is Antman
                Avengers.remove(partner)
                played_Avengers.append(partner)
                health -= 80
                print(f"You got injured and your health is at {health}%")
                if health <= 0:
                    health = 0
                    print("You died.")
                    time.sleep(0.5)
                    tprint("GAME OVER")
                    time.sleep(0.5)
                    sys.exit('Thank you for playing.')
                else:
                    print("It was a hard fight but somehow, you won.")
                    time.sleep(0.5)
                    stones.remove('Mind Stone')
                    infinity_gauntlet.append('Mind Stone')
                    print("You returned home using the Space Stone.")
                    time.sleep(0.5)
                    enter()
                    clear()
                    free_roam()
            else:
                health = 0
                print(f"{partner} was no match for Ultron.")
                time.sleep(0.5)
                print("You died.")
                time.sleep(0.5)
                tprint("GAME OVER")
                time.sleep(0.5)
                sys.exit('Thank you for playing.')
        else:
            print("You use Space Stone to teleport where Ultron is.")
            time.sleep(0.5)
            print(f"You and, {partner} suddenly teleport to a dark space.")
            print("You died because you couldn't breath.")
            tprint("GAME OVER")
            time.sleep(0.5)
            sys.exit('Thank you for playing.')
          
def eye_of_agamotto():
    """
    This room has the Time Stone
    """
    global Avengers
    global played_Avengers
    global name
    global health
    global infinity_gauntlet
    global location
    global stones
    location = "Mirror Dimension"
    status()
    print("Dr. Strange: Time Stone is the hands of Kaecilius.")
    time.sleep(0.5)
    print("Dr. Strange: He is a wizard just like me.")
    time.sleep(0.5)
    print("Dr. Strange: He is currently hidden in mirror dimension.")
    time.sleep(0.5)
    print("Dr. Strange: It will be impossible to find him using space stone.")
    time.sleep(0.5)
    print("Dr. strange: So, this time, I shall go with you to retrive the Time Stone.")
    time.sleep(0.5)
    print("Dr. Strange opened a portal to mirron dimention. You and Dr. Strange entered the mirror dimension.")
    time.sleep(0.5)
    print("World seemed scrambled in the mirror dimention.")
    time.sleep(0.5)
    print("You could not tell up from down.")
    time.sleep(0.5)
    print("Kaecilius: So, you finally came. I was waiting for you.")
    time.sleep(0.5)
    print("The battle begin immediately.")
    time.sleep(0.5)
    print("It was a very intense battle.")
    time.sleep(0.5)
    health = 10
    print(f"You got injured and, your health is at {health}%")
    print("You barely survived this battle.")
    time.sleep(0.5)
    print("You have now obtained the time stone.")
    time.sleep(0.5)
    stones.remove('Time Stone')
    infinity_gauntlet.append('Time Stone')
    enter()
    clear()
    free_roam()
    
def soul():
    """
    This room has the Soul Stone
    """
    global location
    global Avengers
    global stones
    location = "Vormir"
    status()
    print("Dr. Strange: Soul Stone is in a planet called Vormir. It is guarded by Red Skull.")
    time.sleep(0.5)
    print("Dr. Strange: For this mission. You need to be ready to let an avenger die.")
    time.sleep(0.5)
    print("Dr. Strange: And the avenger you pick should be ready to give up his life to save the universe.")
    time.sleep(0.5)
    print("Dr. Strange: Who do you choose?")
    time.sleep(0.5)
    partner = pyip.inputMenu(Avengers, lettered=False, numbered=True)
    if partner == "Dr. Strange": #If partner is Dr. Strange
        print("Sorry, I can't give up my life right now.")
        time.sleep(0.5)
        print("There are things I still have to do.")
        time.sleep(0.5)
        print("Think about it for a while and come back again.")
        time.sleep(0.5)
        enter()
        clear()
        free_roam()
    elif partner == "Thor": #If partner is Thor
        location = "Vormir"
        print("You went to Vormir with Thor. But turns he is immortal and cant die.")
        time.sleep(0.5)
        print("You return home empty handed.")
        time.sleep(0.5)
        enter()
        clear()
        free_roam()
    else:
        location = "Vormir"
        print(f"You went to Vormir with {partner}.")
        time.sleep(0.5)
        print("Vormir was a planet just like earth except it was red.")
        time.sleep(0.5)
        print(f"Red Skull showed you how to obtained the Soul Stone.")
        time.sleep(0.5)
        print(f"{partner} gave his life to retrive the Soul Stone.")
        time.sleep(0.5)
        print(f"You return home with Soul Stone alone.")
        time.sleep(0.5)
        stones.remove('Soul Stone')
        infinity_gauntlet.append('Soul Stone')
        Avengers.remove(partner)
        played_Avengers.append(partner)
        enter()
        clear()
        free_roam()

def use_gauntlet(use_stone, partner, infinity_stone):
    """
    This function makes use of the power of infinity stones
    """
    global health
    global stones
    global infinity_gauntlet
    global played_Avengers
    status()
    if use_stone == "Space Stone": #If power of the Space Stone is used
        print("You and your partner used Space Stone and teleported back to your home")
        time.sleep(0.5)
        enter()
        clear()
        free_roam()
    elif use_stone == "Reality Stone": #If power of the Reality Stone is used
        health = 100
        Avengers.remove(partner)
        played_Avengers.append(partner)
        print("You used Reality Stone and, reality changed in your favor. You won the fight.")
        time.sleep(0.5)
        print(f"You retrived the {infinity_stone}.")
        time.sleep(0.5)
        stones.remove(infinity_stone)        
        infinity_gauntlet.append(infinity_stone)
        print(f"You returned home with {infinity_stone}")
        time.sleep(0.5)
        enter()
        clear()
        free_roam()
    elif use_stone == "Power Stone": #If power of the Power Stone is used
        Avengers.remove(partner)
        played_Avengers.append(partner)
        print("You used Power Stone and, suddenly became very powerful for your opponent. You won the fight.")
        time.sleep(0.5)
        print(f"You retrived the {infinity_stone}.")
        time.sleep(0.5)
        stones.remove(infinity_stone)        
        infinity_gauntlet.append(infinity_stone)
        print(f"You returned home with {infinity_stone}")
        time.sleep(0.5)
        enter()
        clear()
        free_roam()        
    elif use_stone == "Mind Stone": #If power of the Mind Stone is used
        Avengers.remove(partner)
        played_Avengers.append(partner)
        print(f"You used Mind Stone and, your opponent surrendered and, gave you the {infinity_stone}.")
        time.sleep(0.5)
        stones.remove(infinity_stone)        
        infinity_gauntlet.append(infinity_stone)
        print(f"You returned home with {infinity_stone}")
        time.sleep(0.5)
        enter()
        clear()
        free_roam() 
    elif use_stone == 'Time Stone': #If power of the Time Stone is used
        print(f"You used Time Stone and, reversed the time. And it was like this fight never happended.")
        time.sleep(0.5)
        enter()
        clear()
        free_roam()
    elif use_stone == 'Soul Stone': #If power of the Soul Stone is used
        Avengers.remove(partner)
        played_Avengers.append(partner)
        print(f"You used Soul Stone.")
        time.sleep(0.5)
        dead = ["Scarlet Witch", "Hulk", "Captain Marvel", "Vision"] #Dead strong Avengers
        choose = random.choice(dead) #Revivs a dead Avenger
        played_Avengers.append(choose)
        print(f"Suddenly {choose} came back from dead and, helped you win the fight.")
        time.sleep(0.5)
        stones.remove(infinity_stone)        
        infinity_gauntlet.append(infinity_stone)
        print(f"You returned home with {infinity_stone}")
        time.sleep(0.5)
        enter()
        clear()
        free_roam()
    else:
        sys.exit("The Universe suddenly collopsed.")

def talk():
    """
    This functions allows you to talk with Dr. Strange and go on missions.
    """
    global name
    global gauntlet
    global king_eitri_met
    global Avengers
    global played_Avengers
    global location
    global infinity_gauntlet
    location = "Home"
    status()
    print('You decided to talk with Dr. Strange about the infinity stones.')
    time.sleep(0.5)
    if gauntlet == False: #If you don't have the infinity gauntlet
        if king_eitri_met == False: #If you haven't met King Eitri before
            print("Dr. Strange: The power of infinity stones are not something, a normal human like you can handle. So, I suggest that you look for infinity gauntlet first.")
            time.sleep(0.5)
            print(f"{name.title()}: Where do I find one?")
            time.sleep(0.5)
            print("Dr. Strange: There is a neutron star,Nidavellir. It is the home of the Dwarves.")
            time.sleep(0.5)
            print("Dr. Strange: There you will find King Eitri. You have to convince him to make you an Infinity Gauntlet.")
            time.sleep(0.5)
            print(f"{name.title()}: That sounds fun but how am I going to travel all the way to a neutron star. That I didn't even knew existed a moment ago.")
            time.sleep(0.5)
            print("Dr. Strange: That's where I come in.")
            time.sleep(0.5)
            print("Dr. Strange begins to circle his hands around.")
            time.sleep(0.5)
            print("Dr. Strange: Here, I have opened a portal to Nidavellir. This will be open until you return back. Good Luck!!!")
            time.sleep(0.5)
            print("You enter the portal.")
            time.sleep(0.5)
            enter()
            clear()
            nidavellir()
        elif king_eitri_met == True: #If you have met King Eitri before
            print(f"{name.title()}: I would like to travel to Nidavellir again. Can you open the portal to Nidavellir?")
            time.sleep(0.5)
            print("Dr. Strange: Sure")
            time.sleep(0.5)
            print("Dr. Strange opened the portal to Nidavellir. And, you entered through the portal.")
            time.sleep(0.5)
            enter()
            clear()
            nidavellir()
    elif (gauntlet == True) and ('Space Stone' not in infinity_gauntlet): #If you have gauntlet but not the Space Stone
        print("Dr. Strange: Since you have already collected an infinity gauntlet. Next you have to collect all the infinity stones.")
        time.sleep(0.5)
        print("Dr. Strange: But I suggest that you collect space stone first. Killmongor has the space stone.")
        time.sleep(0.5)
        print(f"{name.title()}: Why?")
        time.sleep(0.5)
        print("Dr. Strange: Two Reasons. First it is on earth and second you will not need me to teleport you, if you have the space stone with you.")
        time.sleep(0.5)
        print(f"{name.title()}: Ok, I will retrive the space stone first then.")
        time.sleep(0.5)
        print("Dr. Strange: Before you go. You can choose one avenger to take with you on this mission.")
        time.sleep(0.5)
        print("Dr. Strange: Remember that if you choose an avenger once. They will not be available for rest of the mission.")
        time.sleep(0.5)
        print("Dr. Strange: Who do you choose?")
        time.sleep(0.5)
        partner = pyip.inputMenu(Avengers, lettered=False, numbered=True)
        Avengers.remove(partner)
        played_Avengers.append(partner)
        print(f"Dr. Strange begin to circle his hands again and suddenly {partner} entered the room.")
        time.sleep(0.5)
        print("Dr. Strange begin to circle his hand again and another portal opened.")
        time.sleep(0.5)
        print("Dr. Strange: This is where you will find the Space Stone.")
        time.sleep(0.5)
        print(f"You and {partner} enter the portal and landed on Wakanda.")
        time.sleep(0.5)
        enter()
        clear()
        tesseract(partner)
    elif len(stones) > 1: #If you have the Space Stone
        print("Now that you have collected the Space Stone. You are free to choose which ever stone you want to retrive next.")
        time.sleep(0.5)
        print("Which stone do you want to retrive?")
        time.sleep(0.5)
        stone = pyip.inputMenu(stones, lettered=False, numbered=True) #You choose which stone to retrive
        if stone == 'Reality Stone':
            enter()
            clear()
            aether()
        elif stone == 'Power Stone':
            enter()
            clear()
            power()
        elif stone == 'Mind Stone':
            enter()
            clear()
            mind()
        elif stone == 'Time Stone':
            enter()
            clear()
            eye_of_agamotto()
        elif stone == 'Soul Stone':
            enter()
            clear()
            soul()
        else:
            sys.exit("The Universe suddenly collapsed.")
    elif len(stones) == 1: #If only one stone is left to retrive
        print("Let's retrive the last stone.")
        stone = stones[-1]
        if stone == 'Reality Stone':
            enter()
            clear()
            aether()
        elif stone == 'Power Stone':
            enter()
            clear()
            power()
        elif stone == 'Mind Stone':
            enter()
            clear()
            mind()
        elif stone == 'Time Stone':
            enter()
            clear()
            eye_of_agamotto()
        elif stone == 'Soul Stone':
            enter()
            clear()
            soul()
        else:
            sys.exit("The Universe suddenly collapsed.")
    elif len(stones) == 0: #If all the stones are collected
        enter()
        clear()
        end()
    else:
        sys.exit("The universe suddenly collapsed.")

def free_roam():
    """
    This function allows you to be free at your home 
    and gives you the option to 
    regain health, 
    earn coins, 
    go on missions
    and exit the game.
    """
    global location
    location = "Home"
    status()
    print("Remember to regain your health by eating before every mission.\nPlaying Rock Paper Scissors with Dr. Strange earns you money.\n")
    print("You are in your house. What do you want to do?")
    time.sleep(0.5)
    option = pyip.inputMenu(['Eat', 'Play Rock Paper Scissors with Dr. Strange', 'Talk to Dr. Strange', 'Quit'], lettered=False, numbered=True)
    clear()
    if option == 'Eat': #Option 1
        eat()
    elif option == 'Play Rock Paper Scissors with Dr. Strange': #Option 2
        game()
    elif option == 'Talk to Dr. Strange': #Option 3
        talk()
    else: #Option to exit the game
        sys.exit('Thank you for playing.')

def end():
    """
    The ending of the game
    """
    global name
    status()
    print("Dr. Strange: Congratulations!, you have successfully retrive all the infinity stones.")
    time.sleep(0.5)
    print("Dr. Strange: Now it's time to revive everyone that Thanos killed.")
    time.sleep(0.5)
    print("Dr. Strange: Who do you think should use the stones to bring everyone back.")
    time.sleep(0.5)
    print(f"{name.title()}: I think Thor should do it. Since, he is a god and is immortal.")
    time.sleep(0.5)
    print(f"Thor: Give me the stones.")
    time.sleep(0.5)
    print(f"You hand over the stones to Thor.")
    time.sleep(0.5)
    print(f"He snapped his fingers.")
    time.sleep(0.5)
    print(f"Everyone Thanos killed were brought back to life.")
    time.sleep(0.5)
    print(f"You saved the Universe.")
    time.sleep(0.5)
    tprint("YOU WIN.")
    
def main():
    """
    Main Function
    """
    clear()
    intro()
    free_roam()

#Main Function call
main()
