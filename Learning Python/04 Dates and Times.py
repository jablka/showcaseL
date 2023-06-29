# playing with the challenge 
# in chapter 4. Dates and Times
# in course Learning Python by Joe Marini https://www.linkedin.com/learning/learning-python-14393370/
#

import calendar

def countDays(r, m, day):
     cal = calendar.monthcalendar(r, m)
     print('\n(')
     print(f"Takže {m} {r} Listed:\n{cal}")

     print("ideme Loop", len(cal),"krát")
     counter = 0
     for i in cal:
          print(i)
          if i[day] > 0:
               counter += 1
     print(')')
     return counter

cykl = True
while cykl:
     try:
         print("Type 'e' for exit, or follow the instructions.")
         rok = input("rok: ")
         if rok == "e":
              print(f"Typed: {rok}. Program terminated.")
              break
         
         rok = int(rok)

         mesiac = int(input("mesiac (1-12): "))
          
         day_of_week = int(input("deň v týždni (0-6): "))
     
     except Exception as e:
          print("vstup nie je valídny:\n", e, "\nprogram ukončený.")
          break

     vysl = countDays(rok, mesiac, day_of_week)
     
     meno_dna = calendar.day_name[day_of_week]
     print(f"\n{meno_dna} sa vyskytuje {vysl} krát.\n") 

