#starts loop
while True:
    #attempt to retrieve integer
    try:
        #prompts user for width and passes to integer
        width = int(input('Width: '))
    #catches invalid entries
    except ValueError:
        #error message
        print('Invalid. Please enter a number.')
        #continues loop
        continue
    #checks that there is a positive value that caps at 15
    if width <= 15 and width > 0:
        #ends loop
        break

    elif width <= 0:
        print('Invalid (MIN 1)')
        continue
    else:
        print('Invalid (MAX 15)')
        continue
   
#starts loop
while True:
    #attempt to retrieve integer
    try:
        #prompts user for height and passes to integer
        height = int(input('Height: '))
    #catches invalid entries
    except ValueError:
        #error message
        print('Invalid. Please enter a number.')
        #continues loop
        continue
    if height <= 15 and height > 0:
        #ends loop
        break
    elif height <= 0:
        print('Invalid (MIN 1)')
        continue
    else:
        print('Invalid (MAX 15)')
        continue

#sets a counting variable
count = 0
#sets row as an empty string
row = ''
#sets * to variable to fill in borders
dot = '* '

#creates top and bottom rows
while count < width:
    row = row + dot
    count += 1

#sets first count variable
count1 = 0
#prints top row
print(row)
#uses count to determine amount of middle rows
while count1 < height - 2:
    #resets second count with each row
    count2 = 0
    #adds a * to first index in string
    middleRows = dot
    #adds empty spaces for each row
    while count2 < width - 2:
        middleRows = middleRows + '  '
        count2 += 1
    #adds closing *
    middleRows = middleRows + dot
    #prints the new string
    print(middleRows)
    count1 += 1
#prints bottom row
print(row)