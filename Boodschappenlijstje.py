
boodschapen_dic = {}

def geen_boodschappen_meer():
    x = input("Wilt u nog een keer bestelen? (y/n) : ")
    if x == "y":
        print("Done")
        print(boodschapen_dic)
        return
    elif x == "n":
        program()
    
        
def program():
    while True :
        boodschapen_input = input("Voeg een item toe aan de lijst aub  : ")
        a = 1
        if boodschapen_input in boodschapen_dic.keys():
            a = a + 1
            boodschapen_dic.update({boodschapen_input : a }) 
            geen_boodschappen_meer()
            break 
        else :
            boodschapen_dic[boodschapen_input] = a
            geen_boodschappen_meer()
            break

program()




