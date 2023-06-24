def factorial(k):
    fact = 1
    for i in range(1, k+1):
        fact = fact * i
    return fact


def euler(n):
    e = 1.0
    for i in range(1, n+1):
        e += 1/factorial(i)
    return e


def main():
    print('eular(20) = {0:10.5f}'.format(euler(20)))

main()