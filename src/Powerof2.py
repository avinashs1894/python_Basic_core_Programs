'''
Created on 03-Dec-2021

@author: DELL
'''

try:
    power = int(input("Enter A power:"))
    if power >31:
        raise ValueError("Entered A Number Greater Than 31")
    number = 1
    for i in range(power):
        number = number *2
        print(number)

except ValueError: 
    print("Invalid Input")
