#sets num1 equal to 1
num1 = 1
#creates a loop until num1 increments to 11
while num1 <= 10:
    #sets num2 equal to 1 with each num1 iteration
    num2 = 1
    #begins num2 iterations
    while num2 <= 10:
        #saves total for each change in num2
        total = num1 * num2
        #prints result immediately to console
        print('%d X %d = %d' % (num1, num2, total))
        #increments num2
        num2 += 1
    #increments num1   
    num1 += 1
    