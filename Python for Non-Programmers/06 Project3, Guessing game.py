import random
import time

print("Ahoj, vitaj v hre.")
time.sleep(0.5)
print("\nvyberám si číslo od 1 do 100.")

time.sleep(0.5)
print("\nwait", end = "")

for i in range(10):
    print('.', end = "", flush=True)
    time.sleep(0.15)
print("\n\nmám vybraté.")

correct = random.randint(1,100)

time.sleep(0.5)
guess = int(input("\naký je tvoj tip? "))
x=1 

while guess != correct:
  print('\nwait', end = "", flush=True)
  for i in range(5):
      print('.', end = "", flush=True)
      time.sleep(0.15)
  
  if guess > correct:
     print(" nesprávne, musíš ísť nižšie")
  else:
     print(" nesprávne, musíš ísť vyššie")
    
  guess = int(input("\naký je tvoj tip? "))
  x+=1
  
print(f"\n Áno, blahoželám! Trvalo ti to {x} krát")
