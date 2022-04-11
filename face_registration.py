# Script that takes images of users face from varying angles.
# Stores each one of these in a directory within dataset
# User choses username of directory e.g. cam
# Validation on that name, against previous dirs and excludiding non letter characters.
# Then runs faces_training to add new user to the program.
import cv2
import os
from time import sleep

# functions
    # name collection and validation.
def name_collection(user):
    # Validation: At least one alphabet character, allows for spaces.
    if(any(x.isalpha() for x in user)
    and all(x.isalpha() or x.isspace() for x in user)):
        # Converts user to lower case and whitespaces to '-'
        user = user.lower()
        user = user.replace(" ","-")
        username = user
        print("The name you entered is: {}\n".format(user))
        print("Would you like to continue with the name '{}'?\n".format(username))
        a = input('Type yes or y and press enter to continue:')
        if a == "yes" or a == "y":
            return username
        else:
            return 1
    else:
        print("Please try again.")
        return 1

# face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
# cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

# Welcome message.
print("*==========================  WELCOME   ==========================*\n")
print("|    To begin please enter a (user) name you would like to use.  |\n")
print("|    White spaces will be substituted with a dash.               |\n")
print("|    Otherwise your name should only contain letters.            |\n")
print("*================================================================*\n")

newUser = name_collection(input('Enter name:-'))
while newUser == 1:
    newUser = name_collection(input('Enter name:-'))
else:
    print(newUser)