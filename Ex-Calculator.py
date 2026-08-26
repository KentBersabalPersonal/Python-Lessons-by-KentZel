
print("\n")

choice = input("Enter an operator (+ - * /): ")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if choice == "+":
  result = num1 + num2
  print(f"Result: {round(result, 3)}")
elif choice == "-":
  result = num1 - num2
  print(f"Result: {round(result, 3)}")
elif choice == "*":
  result = num1 * num2
  print(f"Result: {round(result, 3)}")
elif choice == "/":
  result = num1 / num2
  print(f"Result: {round(result, 3)}")
else:
  print(f"{choice} is not valid")

# This is how you make calculator in Python, mas dali ang syntax :>
