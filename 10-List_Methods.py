scores = [85, 90, 78]

scores.append(95)     # adds a new value to the end
scores.remove(78)     # removes a specific value

print("\nScores:", scores)
print("Highest:", max(scores))
print("Total:", sum(scores))

# OUTPUT IS:
# Scores: [85, 90, 95]
# Highest: 95
# Total: 270

# MAIN IDEA:
# Lists come with built-in functions ("methods") to modify and analyze
# them easily — no manual loops needed for common tasks.

# .append(95)   -> adds a value to the end (like push_back in C++ vectors)
# .remove(78)   -> removes the first matching value
# max(scores)   -> returns the largest value in the list
# sum(scores)   -> adds up every value in the list

# min(scores)   -> this is the opposite of the max one, it returns the smallest value in the list.
