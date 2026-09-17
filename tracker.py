income = float(input("Enter your monthly income (K): "))
transport = float(input("Enter transport cost (K): "))
food = float(input("Enter food cost (K): "))
balance = income - transport - food
print(f"Your remaining is: K{balance}")