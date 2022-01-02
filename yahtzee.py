import random
from tabulate import tabulate
#total punts 

answer = 0
answer2 = 1 
n = []
z = 0
integer = 0
#Dice
l = 0
dice = [1 , 2 , 3 , 4 , 5 , 6]
answe1 = []
table = [["Combinatie" , "Aantal punten"  ] , [ "Three of a kind" , "Totaal aantal ogen "] , ["Four of a kind" , "Totaal aantal ogen"] , ["Full House" , 25] , ["Small Straight" , 30] , ["Large Straight" , 40] , ["Yahtzee" , 50] , ["Chance" , "Totaal aantal ogen"]]
part1_totalx = 0
punts_part2y = 0

#Functions

def part1_total():
    global punts_part1
    global part1_totalx
    values = punts_part1.values()
    sum_part1 = sum(values)
    if sum_part1 >= 63:
        answer = sum_part1 + 63
        print("total part1 : " , answer)
        part1_totalx = answer
        return part1_totalx
    else:
        answer = sum_part1
        print("total part1 : " , sum_part1)
        part1_totalx = answer
        return part1_totalx

def part1n2_total():
    global punts_part2
    global part1_totalx
    values = punts_part2.values()
    sum_part2 = sum(values)
    print("total part2 : " ,sum_part2)
    total = part1_totalx + sum_part2
    print("............................")
    print("total score (part 1 + part 2 ) = " , total)
    


def total_score_results():
    global part1_totalx
    global punts_part2y
    total = part1_totalx + punts_part2y
    print("total score (part 1 + part 2 ) = " , total)
    return total   #total punts of part1 and part2


def roll_func():
    global dice
    global answe1
    for x in range(3):
        i = 5 - len(answe1)
        for l in range(i):
            roll = random.choice(dice)
            print(roll)
        number_t0_keep =  list(map(int,input("Write which numbers you want to keep : ").split()))
        answe1.extend(number_t0_keep)
        print(answe1)
        if len(answe1) == 5:
            break
    while len(answe1) != 5 :
        print(answe1)
        number_t0_keep =  list(map(int,input("Write which numbers you want to keep : ").split()))
        answe1.extend(number_t0_keep)
    
    
def punts_func():
    global answe1
    global answer2
    global z
    global l
    count = 0
    count1 = 0
    for i in answe1:
        if i == 1 and answer2 == "ace" : 
            count = count + 1
            for l in range(1):
                z = 1 * count
                break
        elif i == 2 and answer2 == "twos" : 
            count = count + 1
            for l in range(1):
                z = 2 * count
                break
        elif i == 3 and answer2 == "threes" : 
            count = count + 1
            for l in range(1):
                z = 3 * count
                break
        elif i == 4 and answer2 == "fours" : 
            count = count + 1
            for l in range(1):
                z = 4 * count
                break
        elif i == 5 and answer2 == "fives" : 
            count = count + 1
            for l in range(1):
                z = 5 * count
                break
        elif i == 6 and answer2 == "sixes" : 
            count = count + 1
            for l in range(1):
                z = 6 * count
                break 
        elif i == 1 or 2 or 3 or 4 or 5 or 6 and answer2 == "Three of a kind" : 
            count = count + 1
            if count >= 3:
                print("this :" , count)
                sum_part2 = sum(answe1)
                z = sum_part2
                break
        elif i == 1 or 2 or 3 or 4 or 5 or 6 and answer2 == "Four of a kind" : 
            count = count + 1
            if count >= 4:
                print("this :" , count)
                sum_part2 = sum(answe1)
                z = sum_part2
                break
        elif i == 1 or 2 or 3 or 4 or 5 or 6  and answer2 == "Full" : 
            count = count + 1
            if count == 3:
                l = 30
                for i in answe1:
                    if i == 1 or 2 or 3 or 4 or 5 or 6:
                        count1 = count1 + 1
                        if count == 2:
                            print("this :" , count)
                            l = 30
                            break 
    a = [1 ,1 , 1 , 1 , 1 ]
    b = [2 , 2 , 2 , 2 , 2 ]
    c = [3 , 3 , 3 , 3 , 3]
    d = [4 , 4 , 4 , 4 , 4]
    e = [5 , 5 , 5 , 5 , 5]
    f = [6 , 6 , 6 , 6 , 6]
    k = [1 , 2 , 3 , 4 , 5 ]
    if answe1 == a or b or c or d or e or f  and answer2 == "y" : 
        l = 30 
    elif  answe1 == k and answer2 == "large" : 
        l = 30
    elif  1 and 2 and 3 and 4 and 5 in answe1 and answer2 == "small" : 
        l = 30 
    elif 1 and 2 or 2 and 3  or 3 and 4 or 4 and 5 or 5 and 6 or 6 in answe1 and  answer2 == "chance" :
        sum_part2 = sum(answe1)
        z = sum_part2
        l = 30     
        


def turnlist():
    global z
    global integer
    strings = str(z)
    a_string = "".join(strings)
    integer = int(a_string)
    print(integer)

def print_punts():
    print(".........")
    print(punts_part1)
    print(".........")
    print(punts_part2)
    print(".........")




def add_to_dic():
    global answer2
    global integer
    global l
    if answer2 == "ace":
        punts_part1["ace"] = int(integer)
        print_punts()
    elif answer2 == "twos":
        punts_part1["twos"] = int(integer)
        print_punts()
    elif answer2 == "threes":
        punts_part1["threes"] = int(integer)
        print_punts()
    elif answer2 == "fours":
        punts_part1["fours"] = int(integer)
        print_punts()
    elif answer2 == "fives":
        punts_part1["fives"] = int(integer)
        print_punts()
    elif answer2 == "sixes":
        punts_part1["sixes"] = int(integer)
        print_punts()
    elif answer2 == "Three of a kind":
        punts_part2["Three of a kind"] = int(integer)
        print_punts()
    elif answer2 == "Four of a kind":
        punts_part2["Four of a kind"] = int(integer)
        print_punts()
    elif answer2 == "Full" and l == 30:
        punts_part2["Full House"] = int(25)
        print_punts()
    elif answer2 == "small" and l == 30 :
        punts_part2["Small straigh"] = int(30)
        print_punts()
    elif answer2 == "large" and l == 30:
        punts_part2["Large straight"] = int(40)
        print_punts()
    elif answer2 == "y" and l == 30:
        punts_part2["Yahtzee"] = int(50)
        print_punts()
    elif answer2 == "chance" and l == 30:
        punts_part2["Chance"] = int(integer)
        print_punts()
        


def chose_punts1():
    global answer2
    print("..........")
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    print("..........")
    print("ace")
    print("twos")
    print("threes")
    print("fours")
    print("fives")
    print("sixes")
    print(".......")
    print("Three of a kind")  
    print("Four of a kind")  
    print("Full House")  
    print("Small straigh")  
    print("Large straight")  
    print("Yahtzee")  
    print("Chance")  
    print("........")
    anwer3 = input("chose which points : ")
    answer2 = anwer3


        
                     



#program structure

#1- collections

punts_part1 = {
    "ace" : 0 ,
    "twos": 0 ,
    "threes": 0 ,
    "fours": 0 ,
    "fives": 0,
    "sixes": 0 ,
}



punts_part2 = {
    "Three of a kind" : 0 ,
    "Four of a kind" : 0,
    "Full House" : 0 , 
    "Small straigh" : 0 , 
    "Large straight" : 0 ,
    "Yahtzee" : 0 ,
    "Chance" : 0 ,
}


            

                
            

#program

runs = 13
for i in range (runs):
    print(runs)
    print("press on any button to roll the dice")
    button = input(" : ")
    roll_func()    
    chose_punts1()
    punts_func()
    turnlist()
    add_to_dic()
    answe1.clear()
    runs-=1
print("......................")
print(part1_total())
print(part1n2_total())
