import os
import time

print()
print("Calculator")
print()

while True:
  solve = int(input("Choose a number\n1. Division\n2. Multiplication\n3. Addition\n4. Subtraction\n"))
  time.sleep(1)
  os.system("cls")

  if solve == 1:
    first = float(input("First Number: "))
    second = float(input("Second Number: "))
    result = first / second
    print(f"Answer: {result}")

  elif solve == 2:
    first = float(input("First Number: "))
    second = float(input("Second Number: "))
    result = first * second
    print(f"Answer: {result}")

  elif solve == 3:
    first = float(input("First Number: "))
    second = float(input("Second Number: "))
    result = first + second
    print(f"Answer: {result}")

  elif solve == 4:
    first = float(input("First Number: "))
    second = float(input("Second Number: "))
    result = first - second
    print(f"Answer: {result}")

  print() 
  again = input("Would you like to try a new calculation? ").lower()
  print()
  if again != "yes":
    break