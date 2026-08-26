def greet(name="friend"):
    print("\nHello,", name + "! Welcome to Python.")

greet("Kent")
greet()

# OUTPUT IS:
# Hello, Kent! Welcome to Python.
# Hello, friend! Welcome to Python.

# MAIN IDEA:
# A function parameter can have a default value, used automatically if the caller doesn't provide one — 
# something C/C++ doesn't do the same way without overloading.

# def greet(name="friend"):
#  -> if greet() is called with NO argument, "name" becomes "friend"
#  -> if greet("Kent") is called, "name" becomes "Kent" instead

# Works whenever you want to put value name in the program and if not, it returns in a default given value.
