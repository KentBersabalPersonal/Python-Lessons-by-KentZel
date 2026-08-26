class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("\nHi, I'm", self.name)

s1 = Student("Kent", 20)
s1.introduce()
print("Age:", s1.age)

# OUTPUT IS:
# Hi, I'm Kent
# Age: 20

# MAIN IDEA:
# A class is a blueprint for creating objects — same idea as C++, but the constructor and structure look different.

# def __init__(self, name, age):
#  -> this IS the constructor — it runs automatically when a new
#     Student object is created (equivalent to Student(string, int) in C++)

# self.name = name
#  -> "self" refers to the CURRENT object being created — it's like "this" in C++, but must be written explicitly as the first parameter of every method

# s1 = Student("Kent", 20)   -> creates an object (no "new" keyword needed).
# s1.introduce()   -> calling a method on that object.
