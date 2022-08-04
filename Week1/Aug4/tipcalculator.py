#Creates a loop on exception until valid input.
while True:
    try:
        #attempts to convert user input to int
        bill = float(input('Total bill amount: '))
    except ValueError:
        #prints error message and reprompts user
        print('Please enter a number.')
        continue
    break

#Creates a loop until service level input is valid.
while True:
    #prompts for service rating
    service = input('Level of service (good, fair, bad): ')
    #determines which tip amount to calculate
    if service.lower() == 'good':
        tip = bill * 0.20
    elif service.lower() == 'fair':
        tip = bill * 0.15
    elif service.lower() == 'bad':
        tip = bill * 0.10
    else:
        print('Invalid entry. Please enter good, fair or bad.') 
        continue
    break   

#calculates total
total = bill + tip
#prints results
print("The tip amount is: %.2f" % tip)
print("The total amount is: %.2f" % total)