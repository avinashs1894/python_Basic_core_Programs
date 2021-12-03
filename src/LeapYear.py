'''
Created on 03-Dec-2021

@author: DELL
'''

def checkYear(year):
    return (((year % 4 ==0) and (year % 400 != 0)) or (year % 400 == 0))
year = int(input("enter a year:"))

if(checkYear(year)):
    print("Year is leap year")
else:
    print("Year is not a leap Year")