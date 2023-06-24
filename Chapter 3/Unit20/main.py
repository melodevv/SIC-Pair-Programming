def func1(a):
    def func2():
        result1 = []
        for i in a:
            if i % 5 == 0:
                result1.append(i)
        return result1

    def func3():
        result2 = []
        for i in a:
            if i % 7 == 0:
                result2.append(i)
        return result2

    return func2() + func3()


def main():
    lst = [i for i in range(1, 101)]

    result = func1(lst)

    result.sort()

    print(result)


main()
