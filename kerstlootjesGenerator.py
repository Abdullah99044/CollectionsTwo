import random
from typing import ValuesView

keys = []
dic = {}

Values = []

while True:
    n = len(keys)
    print("Ingevoerd namen" , n)
    anwser = input("Wat is jouw naam? : ")
    if anwser in keys :
        print("Naam is al ingevoerd! schrijf nieuwe naam")
    else:
        keys.append(anwser)
        if len(keys) > 2 :
            anwser1 = input("Wil je starten met lootjes trekken? (y/n) :")
            if anwser1 == "y":
                break
            else:
                print("Is goed! ")
l = n + 1
for i in range(l):
    Values.append(random.randint(1,500))

zip_list = zip(keys , Values)

dic = dict(zip_list)

print(dic)


        
    
