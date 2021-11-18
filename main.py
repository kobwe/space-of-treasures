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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

first_pick = input ("You are stolen by the aliens! choose, what you need to do, hijack their UFO or swear them? (print hijack or swear) ").lower()
if first_pick == "swear":
  print ("They drop you into ocean, game over")
else:
  second_pick = input ("You stole the UFO! Now you must choose where you must fly, to Mars or Venus? \n").lower()
  if second_pick == "venus":
    print ("Oh no, you trapped to the evil aliens :(\n")
  else:
    third_pick = input("Wow! There are so much good aliens! They say that you are their hero and you must kill the dangerous dragon! Which weapon do you choose, sword, railgun or cheese?\n").lower()
    if third_pick == "sword":
      print ("oh no, the skin of this dragon is really strong, he eat you!")
    elif third_pick == "railgun":
      print ("its a useless weapon! All bullets ricochet in you!")
    else:
      print ("Wow! This dragon really love cheese you bring! He give you all treausers he got!\n")
      print ("You win!")
      



