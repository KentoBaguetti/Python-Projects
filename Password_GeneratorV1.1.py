import random
import string

def main():
    password_style = printMenu()
    password = makePassword(password_style)
    print(password)

def printMenu(): # asks the user for the style of password the want. If their input is invalid, the program asks them to restart from the beginning
    while True:
        try:
            length = int(input("Enter the length of password desired: "))
            uppercase = input("Do you require uppercase letters? (y or n): ")
            if uppercase != "y" and uppercase != "n":
                raise Exception
            numbers = input("Do you require numbers?(y or n): ")
            if numbers != "y" and numbers != "n":
                raise Exception
            specialCharacters = input("Do you require special characters?(y or n): ")
            if specialCharacters != "y" and specialCharacters != "n":
                raise Exception
            passwordStyle = (length, uppercase, numbers, specialCharacters) # the style of the password is stored in this tuple which will be used by the makepassword method
            return passwordStyle
        except ValueError:
            print("Please try again.")
        except Exception:
            print("Please try again.")

def makePassword(style):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    specialChars = "!@#$%^&*?"
    
    repertoire = "" + lowercase # the repertoire is just the characters that can be used in the password
    validation = 0 # used for later on in the method. Checks if the password has all the requested types of characters
    if style[1] == "y":
        repertoire += uppercase
        validation += 1
    if style[2] == "y":
        repertoire += numbers
        validation += 1
    if style[3] == "y":
        repertoire += specialChars
        validation += 1
        
    password = "" # an empty string which will hold the password
    validPassword = False
    uppercaseCheck = False
    numberCheck = False
    specialCheck = False
    while not validPassword: # this loop validates if the password is valid, eg contains at least one of each type of character.
        for i in range(0, style[0]):
            password += random.choice(repertoire)
        count = 0
        for j in password:
            if style[1] == "y" and j in uppercase and not uppercaseCheck:
                uppercaseCheck = True
                count += 1
            if style[2] == "y" and j in numbers and not numberCheck:
                numberCheck = True
                count += 1
            if style[3] == "y" and j in specialChars and not specialCheck:
                specialCheck = True
                count += 1
        if count == validation:
            validPassword = True
    return password

main()        
