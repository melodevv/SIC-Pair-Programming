# Q1
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
shortest = s_list[0]
for short in s_list:
    if len(short) < len(shortest):
        shortest = short
print('The shortest string: {}'.format(shortest))

# Q2
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']


def find_longest_string(s_list):
    longest_string = ''
    for string in s_list:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string


longest_string = find_longest_string(s_list)
print("The longest string:", longest_string)

# Q3
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']


def find_shortest_strings(s_list):
    sorted_strings = sorted(s_list, key=len)
    shortest_strings = sorted_strings[:3]
    return shortest_strings


shortest_strings = find_shortest_strings(s_list)
print("The shortest strings:", shortest_strings)
