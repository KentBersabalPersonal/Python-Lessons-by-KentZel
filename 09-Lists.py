grades = [85, 90, 78, 92, 88]

for i in range(len(grades)):
    print("\nGrade", i + 1, ":", grades[i])

# OUTPUT IS:
# Grade 1 : 85
# Grade 2 : 90
# Grade 3 : 78
# Grade 4 : 92
# Grade 5 : 88

# MAIN IDEA:
# A list is Python's version of an array, but more flexible — it can grow, shrink, 
# and hold different types of values without declaring a size upfront.

# grades = [85, 90, 78, 92, 88]  -> creates a list using square brackets
# len(grades)                     -> returns how many items are in the list/len is Length
# grades[i]                       -> accesses the value at position i (index starts at 0, just like arrays)
