def apply_function(func, lst):
    return [func(x) for x in lst]

# Function to double the input
def double(x):
    return x * 2

# Function to square the input
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

doubled_numbers = apply_function(double, numbers)
squared_numbers = apply_function(square, numbers)

print(doubled_numbers)
print(squared_numbers)