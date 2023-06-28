dimensions = []
while len(dimensions) < 2:
    dimension = int(input('Enter n: '))
    dimensions.append(dimension)

multi_dimensional = []
for i in range(dimensions[0]):
    row = [1 if (i + j) % 2 == 0 else 0 for j in range(dimensions[1])]
    multi_dimensional.append(row)

for row in multi_dimensional:
    print(' '.join(map(str, row)))