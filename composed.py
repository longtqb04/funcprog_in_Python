def compose(f, g):
    return lambda x: f(g(x))

def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

composed_function = compose(add_one, multiply_by_two)
result = composed_function(5) #Result: 11