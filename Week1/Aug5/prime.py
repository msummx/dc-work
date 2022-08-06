while True:
    try:
        numberIn = int(input('Please enter a positive integer: '))
    except:
        print('That is not a positive integer.')
        continue
    if numberIn < 0:
        print('That is not a positive integer.')
        continue
    else:
        break

def isPrime(number: int) -> bool:
     if number == 2:
            return True
     else:   
        for x in range(2, number):
            if number % x == 0:
                return False
                break
            else:
                return True

if isPrime(numberIn) == True:
    print(str(numberIn) + ' is a prime number!')
elif isPrime(numberIn) == False:
    print(str(numberIn) + ' is not a prime number!')

