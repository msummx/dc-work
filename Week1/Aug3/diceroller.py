import random
#Allows for use of random module

print("Let's roll a dice!")
#Initial message
diceIn = input('How many sides should it have? (2-20): ')
#assigns user input into diceIn string

try:
    dice = int(diceIn)
except:
    print("That's not a number!")
    exit()
#Converts string into int and discards invalid entries.

if dice > 1 and dice <= 20:
    print("It's rolling...")
    result = random.randint(1, dice)
    print("It's a " + str(result) + "!")
#Checks parameters, fetches result, and displays as string.   
else:
    print("That's not a valid number!")
#Message if parameters are not met.



