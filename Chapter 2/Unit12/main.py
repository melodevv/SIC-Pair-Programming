# Q1
tup = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3, 9)
most_frequent = {}
for number in tup:
    if number in most_frequent:
        most_frequent[number] += 1
    else:
        most_frequent[number] = 1

highest_frequent = 0
highest_number = 0

for number, frequent_number in most_frequent.items():
    if frequent_number > highest_frequent:
        highest_frequent = frequent_number
        highest_number = number
    elif frequent_number == highest_frequent:
        if number > highest_number:
            highest_number = number

print('Given tuples: {}'.format(tup))
print('The most frequent element: {}'.format(highest_number))

# Q2
given_list = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), '']


filtered_list = [item for item in given_list if item != () and item != [] and item != '']


frequent_element = max(set(filtered_list), key=filtered_list.count)

print("Given tuples:", given_list)
print("The most frequent element:", filtered_list)