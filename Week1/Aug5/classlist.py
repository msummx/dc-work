student1 = {
    "id" : "384291",
    "name" : "Bob",
    "bootcamp" : "DigitalCrafts"
    }

student2 = {
    "id" : "569291",
    "name" : "Sue",
    "bootcamp" : "DigitalCrafts"
    }

student3 = {
    "id" : "832654",
    "name" : "Joe",
    "bootcamp" : "DigitalCrafts"
    }

student4 = {
    "id" : "459320",
    "name" : "Linda",
    "bootcamp" : "DigitalCrafts"
    }

student5 = {
    "id" : "943347",
    "name" : "Peggy",
    "bootcamp" : "DigitalCrafts"
    }

students = [student1, student2, student3, student4, student5]

# def lowerNums(oldList: list) -> None:
#     newList = []
#     for x in oldList:
#         idNum = int(x["id"])
#         if idNum < 500000:
#             newList.append(x)
#     return newList

# print(lowerNums(students))

def listSort(oldList: list) -> list:
    newList = []
    highNumber = 0
    for x in oldList:
        idNum = int(x["id"])
        if highNumber < idNum:
            newList.append(x)
            highNumber = idNum
        else:
            i = 0
            for y in newList:
                newIdNum = int(y["id"])
                if idNum < newIdNum:
                    newList.insert(i, x)
                    break
                i += 1
    return newList

print(listSort(students))
