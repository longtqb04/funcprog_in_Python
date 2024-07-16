def pureFunction(list):
    newList = []
    for i in list:
        newList.append(i + 1)
    return newList

OriginalList = [1, 3, 5, 7]
ModifiedList = pureFunction(OriginalList)

print(OriginalList)
print(ModifiedList)