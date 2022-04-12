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
        # Verificiation that username is what user intended.
        print("The name you entered is: {}\n".format(user))
        print("Would you like to continue with the name '{}'?\n".format(username))
        a = input('Type yes or y and press enter to continue:')
        # Begins to check to see if the user already exists in the dataset.
        parent_directory = "dataset/"
        path = os.path.join(parent_directory, username)
        if a == "yes" or a == "y":
            if os.path.isdir(path):
                print("This user already exists, please try again.\n")
                return 1
            else:
                return username # Returns username if it meets all criteria.
        else:
            return 1
    else:
        print("Please try again.")
        return 1
    # Directory creation function for dataset.
def directory_creation(username):
    parent_directory = "dataset/"
    path = os.path.join(parent_directory, username)
    os.mkdir(path)
    print("Directory {} has been created.\n".format(path))


face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)


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
    directory_creation(newUser)
    print("Hello {},\nWe will now begin by scanning your face.".format(newUser))

# while(True):
#     ret, frame = cap.read()
#     frame = cv2.flip(frame, 0)
#     cv2.imshow(newUser,frame)
#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()