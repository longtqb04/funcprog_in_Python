def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

def call_function(func, name):
    return func(name)

print(call_function(greet, "Adam"))  # Output: Hello, Alice!
print(call_function(farewell, "Eva"))  # Output: Goodbye, Bob!