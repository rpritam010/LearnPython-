'''The below picture has been taken from url :- https://ascii.co.uk/art/treasure'''

print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[PRITAM]
*******************************************************************************
''')

print("Welcome to tresure Island.")
print("Your mission is to find the tresure")
choice1 = input('you\re at a crossroad,where you want to go ? type "left" or "right" .').lower()

if choice1 == "left":
    #continue the game
    choice2 = input('You\'ve have come to a lake .There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input("You have arrived at the island unharmed. there is a house with 3 doord ,One red, one yellow, and blue. Which door colour do you choose").lower()
        if choice3 =="red":
            print("Game over")
        elif choice3 == "yellow":
            print("You found the treasure !you win!")
        elif choice3 == "blue":
            print("you enter the room of beast. Game over!.")
        else:
            print("You got attact by an angry trout. Game over. ")

    else:
        print("You got attack by an angry trout. Game Over.")    
    
else:
    print("Game is over")

    