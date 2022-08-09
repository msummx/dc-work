numbers = (input('Please enter a number that has at least three characters: '))

try:
    checkInt = int(numbers)
    if len(numbers) > 2:
        palindrome = numbers[::-1]
        if numbers == palindrome:
            print('The number %s is a palindrome!' % numbers)
        else:
            print('The number %s is not a palindrome!' % numbers)
    else:
        print('Invalid entry.')
except:
    print('Invalid entry.')
        