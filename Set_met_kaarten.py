import random

card = []
a = ["boer " , "vrouw ", "heer " ,"aas " ]
colors = ["harten ", "klaveren ", "schoppen ", "ruiten "]
joker = ["joker" , "joker"]
deck = []

for i in range (2,14):
    card.append(str( i))

for j in range (4):
    card.append(a[ j])


for k in range(4):
    for i in range(13):
        card1 = (colors[k] + card[ i] )
        deck.append(card1)

for n in range(2):
    deck.append(joker[n])


random.shuffle(deck)

for i in range (7):
    z = random.choice(deck)
    print(z)
    deck.remove(z)

print(deck)



