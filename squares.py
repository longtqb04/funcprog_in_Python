def square(x):
    return x * x

def listSquare(numbers):
    squares = map(square, numbers)
    return list(squares)

numbers = [1, 2, 3, 4, 5]
result = listSquare(numbers)
print(result)
#Output: [1, 4, 9, 16, 25]