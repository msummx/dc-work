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

def fact(number: int) -> int:
    x = 2
    y = 1
    while x <= number:
        y = y * x
        x += 1
    return y

print(fact(numberIn))
        
    

    
            
        


