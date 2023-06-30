# program uses this API to retrieve jokes:
# https://github.com/15Dkatz/official_joke_api
# https://official-joke-api.appspot.com/random_joke

import requests
import time

url = 'https://official-joke-api.appspot.com/random_joke'

print("\nVitajte na vtipovisku!")

key = ''
while key != 'q':      
    print('...načítavam vtip, wait...')
    response = requests.get(url)
    vtip = response.json() 

    print()
    print(f'->{vtip["setup"]}')
    print('>>press Enter<<')
    input()
    print(f'->{vtip["punchline"]}')
    print("---HAHA---")
    time.sleep(2)

    print()
    print("press Enter to continue, or type: 'q'+Enter to quit.")
    key = input()
