import random

lucky_number = random.randint(1,100)

fortune_number = random.randint(1,3)

fortune_text = ''

if fortune_number == 1: 
  fortune_text = "Skvelý deň!"

if fortune_number == 2:
  fortune_text = "Ťažký deň, ale dáš to."

if fortune_number == 3:
  fortune_text = "Oženíš sa / vydáš sa!"

# f string
print(f"{fortune_text} A tvoje stastne cislo je {lucky_number}")
