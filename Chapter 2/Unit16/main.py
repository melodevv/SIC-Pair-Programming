mylist = [(1, 2), (4, 5), (4, 2), (3, 1), (9, 4)]

a, b = map(int, input("Enter two integers: ").split())

found_ab = False
found_ba = False
index = None

for i, (m, n) in enumerate(mylist):
    if (m, n) == (a, b):
        found_ab = True
        index = i
        break
    elif (m, n) == (b, a):
        found_ba = True
        index = i
        break

if found_ab:
    print(f"There is ({a},{b}) at the first.")
elif found_ba:
    print(f"There is no ({a},{b}) but there is ({b},{a}) at the {index + 1}st.")
else:
    print(f"There is no ({a},{b}) nor ({b},{a}).")
