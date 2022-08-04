try:
    numberIn = input('Please input a number: ')
    number = int(numberIn)
#Attempts to convert a user input string into integer
except: 
    print('Invalid entry.')
#Catches errors and prevents program from crashing.

if number % 2 == 0:
    print('The number ' + numberIn + ' is even!')
else:
    print('The number ' + numberIn + ' is odd!')
#Checks if there is a remainder and displays message for each case.