#sets coins to 0 and prints to user
coins = 0
print('You have %d coins.' % coins)

#sets up loop to continue prompt until exit
while True:
    #assigns yes or no to decision
    decision = input('Do you want another? (y/n) ')
    #allows for two inputs in yes or no decision
    if decision.lower() == 'yes' or decision.lower() == 'y':
        #increments coin and prints total to console
        coins += 1
        print('You have %d coins.' % coins)
    elif decision.lower() == 'no' or decision.lower() == 'n':
        #prints bye message and breaks loop
        print('Bye.')
        break
    else:
       #prints error message and reprompts
        print("Sorry, didn't catch that. ")
        
