

 
import random
######################################
# Karten maken
######################################

deck = []
total_score = 0
def Deck():
    global deck
    colours = ["Rood ", "Groon ", "Geel ", "Blauwe "]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Neem-Twee", "Sla-buurt", "Keer-om"]
    wilds = ["Keeuzkaart", "Keeuzkaart Neem-vier"]
    
    for colour in colours:
        for value in values:
            cardVal = "{} {}".format(colour, value)
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)
    
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    
    return deck

######################################
# Shuffel deck
######################################

def shuffl(deck):
    for card in range(len(deck)):
        rand = random.randint(0, 107)
        deck[card], deck[rand] = deck[rand], deck[card]
    return deck

def drawCards(numCards):
    global unoDeck
    cardsDrawn = []
    for x in range (numCards):
        cardsDrawn.append(unoDeck.pop(0))
    return cardsDrawn

######################################
#  regels van het spel
######################################

def canPlay(colour , value , playerHand):
    for card in playerHand:
        if "Keeuzkaart" in card:
            return True
        elif  colour in card  or   value in card:
            return True
    return False

######################################
#Print de karten van de spelers
######################################

def showHand(player , playerHand):
    print("Player {} buurt ".format(player+1))
    print("Your hand")
    print("------------")
    y = 1
    for card in playerHand:
        print("{}) {}".format(y , card))
        y+=1
    print("")
######################################
#Ai functie
######################################

def ai_function(color , value  , card):
    global cardChosen
    if  color in card and value in card :
        cardChosen = color and value in card 
        return cardChosen
    elif color in card :
        cardChosen = color in card
        return cardChosen
    elif value in card :
        cardChosen = value in card
        return cardChosen

######################################
#Score functie
######################################

def score( card):
    global total_score
    punten1 = 0
    punten4 = 0
    a = "Keer-om"
    print(card)  
    for card in card: 
        if   "Keer-om"   in card :
            punten1+=20 
           
        elif  "Neem-Twee"  in card :
            punten1+=20 
        elif  "Sla-buurt"  in card : 
            punten1+=20 
        elif "Keeuzkaart" in card:  
            punten4+=50
        elif "1" in card:
            punten1+=1
        elif "2" in card:
            punten1+=2
        elif "3" in card:
            punten1+=3
        elif "4" in card:
            punten1+=4
        elif "5" in card:
            punten1+=5
        elif "6" in card:
            punten1+=6
        elif "7" in card:
            punten1+=7
        elif "8" in card:
            punten1+=8
        elif "9" in card:
            punten1+=9
         

     
    total_score = punten1  + punten4
      
    print("Winnar score is : {}".format(total_score))

######################################
#Het spel
######################################

#Deck variablen

unoDeck = Deck()
unoDeck = shuffl(unoDeck)
unoDeck = shuffl(unoDeck)
discard = []
 
#Hier tellen we de AI spelers die het spel zullen spelen 

players = []
kleuren = ["Rood ", "Groon ", "Geel ", "Blauwe "]
number_of_players = int(input("Hoveel spelers? : "))
while number_of_players < 2 or number_of_players   > 10:
    number_of_players = int(input("Fout! spelers moeten zijn tussen 2 en 10 : "))

for j in range(number_of_players):
    players.append(drawCards(7))

#Hier ik spilt de karten in list vorm 
    
cardChosen = 0
playerTurn = 0
playerDirection = 1 
playing = True
discard.append(unoDeck.pop(0))
splitCard = discard[0].split(" ", 1)
print(splitCard)
currnetColour = splitCard[0]

#Card val is de value van het kaart bijvoorbeeld nummer 0 tot met 9 of "Neem-Twee", "Sla-buurt", "Keer-om"
if currnetColour != "Keeuzkaart":
    cardVal = splitCard[1]
else:
    cardVal = "any"

while playing:
    showHand(playerTurn , players[playerTurn])
    print("kaarten bovenop de aflegstapel {}".format(discard[-1]))
    if canPlay(currnetColour , cardVal , players[playerTurn]):
        ai_function(currnetColour , cardVal  , players[playerTurn])
        discard.append(players[playerTurn].pop(cardChosen-1))
        if len(players[playerTurn]) == 0:
            winner = "Player {}".format(playerTurn+1)
            result = sum(players, [])
            score(result)
            playing = False
        else:      #Dit zijn regels van het special karten
            splitCard = discard[-1].split(" ", 1)
            currnetColour = splitCard[0]
            if len(splitCard) == 1:
                cardVal = "Any"
            else:
                cardVal = splitCard[1]
            if currnetColour == "Keeuzkaart" :
                for x in range (len(kleuren)):
                    print("{} ) {}".format(x+1 , kleuren[x]))
                newColor = random.randint(1,4)
                currnetColour = kleuren[newColor-1]
            if cardVal == "Keer-om":
                playerDirection = playerDirection * -1
            elif cardVal == "Sla-buurt":
                playerTurn += playerDirection
                if playerTurn >= number_of_players:
                    playerTurn = 0
                elif playerTurn < 0:
                    playerTurn = number_of_players-1
            elif cardVal ==  "Neem-Twee":
                playerDraw =  playerTurn+playerDirection
                if playerDraw == number_of_players:
                    playerDraw = 0
                elif playerDraw < 0:
                    playerDraw = number_of_players-1
                players[playerDraw].extend(drawCards(2))
            elif cardVal ==  "Neem-vier":
                playerDraw =  playerTurn+playerDirection
                if playerDraw == number_of_players:
                    playerDraw = 0
                elif playerDraw < 0:
                    playerDraw = number_of_players-1
                players[playerDraw].extend(drawCards(4))
            print(" ")
    else:
        print("Je kan niet spelen! neem een kaart.")
        players[playerTurn].extend(drawCards(1))
    print("")
    

    playerTurn += playerDirection
    if playerTurn >= number_of_players:
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = number_of_players-1
print("Goed gedaan!")
print("")

