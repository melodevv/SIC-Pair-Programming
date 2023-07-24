def int_to_roman(num):
    result = ''
    keys = list(table.keys())
    for i in range(len(keys) - 1):
        while num - keys[i] >= 0:
            result += table[keys[i]]
            num -= keys[i]
    return result


table = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
         100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
         10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

num = int(input("Input a number: "))
print(int_to_roman(num))
