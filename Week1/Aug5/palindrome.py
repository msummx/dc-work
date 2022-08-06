wordIn = input('Please enter a word: ')

def isPalindrome(word: str) -> bool:
    backWord = ''
    x = len(word) - 1
    for letter in word:
        backWord = backWord + word[x]
        x -= 1
    if word == backWord:
        return True
    else:
        return False

if isPalindrome(wordIn) == True:
    print(wordIn + ' is a palindrome!')
else:
    print(wordIn + ' is not a palindrome!')
