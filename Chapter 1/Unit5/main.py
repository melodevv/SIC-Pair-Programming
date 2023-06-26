# Q1
number = int(input("Enter a 3-digit integer: "))
hundredth = (number // 100) % 10
is_hundredth = (hundredth == 3)
print(is_hundredth)

# Q2
number = int(input("Enter an integer: "))
is_multiple_of_5 = (number % 5 == 0)
print(is_multiple_of_5)