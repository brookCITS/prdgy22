import json

users = {}

def loadfile():
    try:
        with open("users.json") as file:
            #load json file as string and update the dict



            print("File loaded to program")
            print(users)
    except:
        print("File could not be found")


def createUser(name, email, password1, password2):
    #does the email already exist?
    if email not in users:
        #Do the passwords match? Then add new user to dict

    else:
        print("Error: user with this email already exist\n\n")

def signIn(email, password):
    #verify user and check their password. if matchs return True

def changePassword(email, CurrentPassword, newPassword):
    #your code here


def updateFile():
    #your code here
    
