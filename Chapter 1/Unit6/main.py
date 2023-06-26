age = int(input("Enter age: "))
if age >= 20:
    group = "Adult"
elif age >= 10:
    group = "Youth"
else:
    group = "Kid"
print(group)