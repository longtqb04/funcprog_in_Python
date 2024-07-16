def onetoFive():
    return [1, 2, 3, 4, 5]
    
list = onetoFive()

def addtoList(arr, n):
    return arr.append(n)
    
n = 6
addtoList(list, n)
print(list)