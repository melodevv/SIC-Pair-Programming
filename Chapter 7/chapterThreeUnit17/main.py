def mean3(a, b, c):
    return (a + b + c) / 3


def max3(a, b, c):
    return max(a, b, c)


def min3(a, b, c):
    return min(a, b, c)


def main():
    a, b, c = input('Enter three numbers :').split()
    a, b, c = int(a), int(b), int(c)

    print('The average value of {0}, {1}, {2} is {3}'.format(a, b, c, mean3(a, b, c)))
    print('The maximum value of {0}, {1}, {2} is {3}'.format(a, b, c, max3(a, b, c)))
    print('The minimum value of {0}, {1}, {2} is {3}'.format(a, b, c, min3(a, b, c)))


main()