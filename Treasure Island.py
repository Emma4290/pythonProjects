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

decision1 = input('''You get off your boat and head for shore. Would you like to head left to explore the jungle or right to explore the beach? Choose "left" or "right".\n''')

decision1 = decision1.lower()

if decision1 == "left":
  decision2 = input('''The jungle was a great choice! You find fresh water to drink and some pineapples to eat. You come across a ravine. Do you swing across on a vine or walk further on to find a rope bridge? Choose "vine" or "bridge".\n''')
  decision2 = decision2.lower()

  if decision2 == "bridge":
    decision3 = input('''Thankfully you find a bridge a few hundred metres away. It's not sturdy, but it will do. You come across an unusual house with 3 coloured front doors. You must choose either "blue", "yellow" or "red".\n''')

    decision3 = decision3.lower()

    if decision3 == "red":
      print("There is a hungry lion behind the door. You lose, game over.")

    elif decision3 == "blue":
      print("You rush inside and fall into a shark tank with 3 hungry great white sharks. Game over.")

    elif decision3 == "yellow":
      print("You have found the treasure! Congratulations.")

    else:
      print("Something's not quite right. Start again.")

  else:
    print("The vine snaps, sending you tumbling into the ravine below. Game over.")

else:
  print("You fell into a hole. Game over.")