def factorize(number):
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1
    return factors


numbers = [18, 39, 63, 126, 792]

for number in numbers:
    factors = factorize(number)
    print("Factors of", number, ":", factors)
