print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

cross_path = input("After we take a long walk, we find a cross path. Which path will you choose? Left or Right? ")

if cross_path == "Left":
    swamp = input("There is a swamp what we gonna do, Captain? Are we just run straight or jump? Run or Jump? ")
    if swamp == "Jump":
        print("We did it! Let's find the treasure that we looking for")
        print("The Captain and his Crew went into the Mysterious Temple called Door Temple")
        choose_door = input("There is 3 big door exist in this temple. Red, Blue, Yellow. Which door that'll you choose? Red Blue or Yellow? ")
        if choose_door == "Red":
            print("Congratulation boy! You get the Legendary Treasure!!")
        elif choose_door == "Blue":
            print("OH NOO! You get eaten by a bear... Game Over")
        else:
            print("THE ROOM IS TOO HOT, EVERYBODY BURNED. Gave Over")
    else:
        print("We swallowed into the swamp and die. Game Over")
else:
    sea = input("We have to cross the sea, should we wait for a boat or just swim? Wait or Swim? ")
    if sea == "Wait":
        print("Thank god we arrived to this island. Look.... there is the treasures!!")
        print("But be careful!! The legend said that there is only one treasure in this island. So it could be a trap")
        choose_treasure = input("Which treasure that we choose? Left or Right? ")
        if choose_treasure == "Right":
            print("It's just a Jack Sparrow's Prank. NOTHING HERE!")
        else:
            print("You get cursed by a box monster. Game Over")   
    else:
        print("HOLY COWWW!! THAT'S A BIG SHARKKKK, ARRRGGGHHH")
        print("You get eaten by Guardian Shark. Game Over")

