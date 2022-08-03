import random
#Allows for use of random module

coins = ['heads', 'tails']
#Assigns heads and tails to the variable coins
something = input('Type anything to flip a coin: ')
#Allows for a user to start coin flip at will

if isinstance(something, str):
    print('You flipped a coin!')
    result = random.choice(coins)
    if result == coins[0]:
        print('It is ' + coins[0] + '!')
    else:
        print('It is ' + coins[1] + '!')
#Checks for user input and executes coin flip
else:
    print('Try something else.')
#Failsafe for invalid input