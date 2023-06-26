#Q1
print("1) Addition     2) Subtraction   3) Multiplication   4) Division")
choice = int(input("Enter choice: "))
if choice == 1:
    # Addition
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif choice == 2:
    # Subtraction
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif choice == 3:
    # Multiplication
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif choice == 4:
    # Division
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else:
    print("Entered an incorrect number.")

#Q2
x, y = map(int, input("Enter x,y coordinates: ").split())

if x > 0 and y > 0:
    quadrant = "first"
elif x < 0 and y > 0:
    quadrant = "second"
elif x < 0 and y < 0:
    quadrant = "third"
elif x > 0 and y < 0:
    quadrant = "fourth"
else:
    quadrant = "on the axis"

print(f"In the {quadrant} quadrant")

#Q3
print("Welcome to Yummy Restaurant. Here is the menu:")
print("Burger (enter b)")
print("Chicken (enter c)")
print("Pizza (enter p)")

menu = input("Choose a menu (enter b, c, p): ")

while menu not in ['b', 'c', 'p']:
    print("Enter the menu again:")
    menu = input("Choose a menu (enter b, c, p): ")

if menu == 'b':
    selected_menu = "Burger"
elif menu == 'c':
    selected_menu = "Chicken"
else:
    selected_menu = "Pizza"
print("You chose", selected_menu + ".")