'''
Created on 03-Dec-2021

@author: DELL
'''
def primenum():
    number = int(input("Enter a Number to find Prime Factores:"))
    i=2
    primefactor = []
    while i * i <= number:
        if number % i == 0:
            primefactor.append(i)
            number//= i 
        else:
            i += 1
    if number >1:
        primefactor.append(number)
    return primefactor
primefactor = primenum()
print("Prime Factors are: ", primefactor)