# Q1

PI = 3.141592
radius = float(input("Enter radius: "))
circumference = 2 * PI * radius
area = PI * radius ** 2
print("Circumference = {}".format(circumference))
print("Area =", area)

# Q2
n = 2
print("a n \ta ** n")
for a in range(2, 7):
    result = a ** n
    print(a, n, '\t ', result)
