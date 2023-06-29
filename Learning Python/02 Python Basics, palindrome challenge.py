# playing with the challenge 
# in chapter 2. Python Basics
# in course Learning Python by Joe Marini https://www.linkedin.com/learning/learning-python-14393370/
#

running = True

while running:
    print('>Testujeme palindróm.')
    vstup = input(">napíš niečo (alebo 'exit' pre koniec) : ")
   
    if vstup == "exit" :
        print(">lúčim sa.")
        running = False 
    
    else:
        vstup = vstup.lower()
        print("lower case:", vstup) 

        vstupConverted=""
        for a in vstup:
            if a.isalnum():
                vstupConverted += a
        print("stripped:", vstupConverted)

        if vstupConverted == vstupConverted[::-1]:
            print(">Máme palindróm!\n")
        else:
            print(">Nie je palindróm.\n")
        
