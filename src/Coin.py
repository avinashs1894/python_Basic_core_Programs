import random


def flipcoin():
    head = 0
    tail = 0
    headperesent = 0
    tailperesent = 0
    
    for a in range(1000):
        coin = random.randint(0,1)
        
        if coin == 1:
            head +=1
        else:
            tail +=1
            
            headperesent = head/10
            tailperesent = 100 - headperesent
            
    print("Head Peresent: " +str(headperesent))
    print("Tail Peresent: " +str(tailperesent))
            
flipcoin()