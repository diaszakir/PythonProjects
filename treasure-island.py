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

print("You came to legendary island Laughtale")
print("You walked in to forest and it divides to 2 paths.")
print("Choose left or right:")
direction = input().lower()

if direction == "left":
  print("You chosed left path and after some time you saw a lake")
  print("You understand that you can wait or try your luck and swim")
  print("Choose action swim or wait")
  action = input().lower()
  if action == "wait":
    print("You waited and water dissapeared with sea beasts.")
    print("You continued to walk and reached 3 caves")
    print("Choose door: red, blue, yellow")
    door = input().lower()
    if door == "yellow":
      print("You win and found treasure")
    elif door == "red":
      print("Burned by fire. Game Over")
    elif door == "blue":
      print("Eaten by beasts. Game Over")
    else:
      print("What? Game Over")
  else:
    print("Attacked by sea beast. Game over")
else:
  print("You fall into a hole. Game over")