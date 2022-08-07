def smallest(numberList: list) -> int:
    lowNum = numberList[0]
    for x in numberList:
        if x <= lowNum:
            lowNum = x
    return lowNum

def largest(numberList: list) -> int:
    highNum = numberList[0]
    for x in numberList:
        if x >= highNum:
            highNum = x
    return highNum

def shortest(stringList: list) -> str:
    shortString = stringList[0]
    i = 0
    for x in stringList:
        if len(x) <= len(shortString):
            shortString = x
    for x in stringList:
        if len(x) == len(shortString):
            i += 1
    if i > 1:
        print('There are %d items in the list that tied for shortest. The highest index will be returned.' % i)
    return shortString

def longest(stringList: list) -> str:
    longString = stringList[0]
    i = 0
    for x in stringList:
        if len(x) >= len(longString):
            longString = x
    for x in stringList:
        if len(x) == len(longString):
            i += 1
    if i > 1:
        print('There are %d items in the list that tied for longest. The highest index will be returned.' % i)
    return longString



