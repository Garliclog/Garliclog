#######
# GLCalculator App
# Version 1.0
# Code by Garliclog
#######

# Libraries to import
from cmath import cos, sin, tan
import math

print("Welcome to the GLCalculator")
# Creating a closed while loop to contain the main application functions
active = True
while (active == True):
    
    print("Which operation would you like to carry out?")
    print("1) Addition \n2) Subtraction \n3) Multiplication \n4) Division \n--Degree Values Only--\n5) Get SIN \n6) Get COS \n7) Get TAN")
    operation = input("")

    # Basic Math Operations
    if(operation == "1"):
        # combines the process of inputting numbers and outputting the answer into one neat line of code
        print("Total: " + str(int(input("Enter the first number: ")) + int(input("Enter the second number: "))))
    elif(operation == "2"):
        # Since operations are simple, the code can be reused, replacing only the mathmatical operator symbol
        print("Total: " + str(int(input("Enter the first number: ")) - int(input("Enter the second number: "))))
    elif(operation == "3"):
        print("Total: " + str(int(input("Enter the first number: ")) * int(input("Enter the second number: "))))
    elif(operation == "4"):
        print("Total: " + str(int(input("Enter the first number: ")) / int(input("Enter the second number: "))))

    # Slightly More Advanced Math Operations
    elif(operation == "5"):
        print("Total: " + str(sin(math.radians(int(input("Enter a number: "))))))
    elif(operation == "6"):
        print("Total: " + str(cos(math.radians(int(input("Enter a number: "))))))
    elif(operation == "7"):
        print("Total: " + str(tan(math.radians(int(input("Enter a number: "))))))
        
    # Error Handling
    else:
        print("Sorry, that's not a valid option")

    # Provides an exit to the application, escaping the closed while loop
    if (input("Do you want to make another calculation? [Y/N]\n").upper() == 'N'):
        active = False

print("Thanks For Chosing GLCalculator")
# Exits
