'''
Created on 03-Dec-2021

@author: DELL
'''
def replace(username):
    if(len(username) < 3):
        return "username is not less then 3 char"
    else:
        return "Hello " +username+ " How are you?"
username = input("enter the name: ")
new_message = replace(username)
print(new_message)