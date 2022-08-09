#sets a range for numbers to check
numbers = range(0,100)

reverseOrder = numbers[::-1]        #slices numbers to read backwards
primeNumbers = []       #initalizes empty list to house prime numbers
for x in reverseOrder:          #checks numbers 1 by 1 in reverse order
    isPrime = False             #sets default to False
    number = int(x)         #saves integer x as a variable to use throughout code
    if number == 2:     #forces 2 to be appended if it appears
        primeNumbers.append(number)   
    elif number > 1:        #makes sure the number is positive and higher than 1
        for y in range(2, number):      #cycles through numbers 2 -> number-1
            if number % y == 0:     #checks that there are no factors
                isPrime = False     #keeps isPrime as False
                break
            else:
                isPrime = True      #becomes True only if no numbers are factors
    if isPrime == True:
        primeNumbers.append(number)     #adds number to prime list
        
            

                
    

print(primeNumbers)