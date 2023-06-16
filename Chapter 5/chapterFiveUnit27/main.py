# Swap with temporary Variables:
def swap1(S, x, y):
    t = S[x]
    S[x] = S[y]
    S[y] = t


# Swap with multiple variables:
def swap2(S2, x, y):
    S2[x], S2[y] = S2[y], S2[x]


# S = [10, 20]
# S2 = [50, 100]
# print('Print unswapped list S:', S)
# swap1(S, 0, 1)
# print('Print swapped list (Temp Variable):', S)
# print()
#
# print('Print unswapped list S2:', S2)
# swap2(S2, 0, 1)
# print('Print swapped list (Multi Variable) S2:', S2)

# ==========================================================
#
# Bubble Sorting
#
# ==========================================================

unlist = [50, 30, 40, 10, 20]
#
# listLen = len(unlist)
# counter = 0
#
# for i in range(listLen):
#     print(unlist)
#     for j in range(listLen - 1):
#         if unlist[j] > unlist[j + 1]:
#             unlist[j], unlist[j + 1] = unlist[j + 1], unlist[j]
#             counter += 1
#
# print('Sorted List: ', unlist)
# print('Number of swaps that occuried:',  counter)

# ==========================================================
#
# Selection Sorting
#
# ==========================================================


# Without Swap
def selectionsort1(S):
    R = []
    while len(S) > 0:
        print(R, S)
        smallest = S.index(min(S))
        R.append(S[smallest])
        S.pop(smallest)
    return R


# stlist = selectionsort1(unlist)
# print(stlist)


# With Swap (In-Place selection)
def selectionsort2(S):
    n = len(S)
    for i in range(n - 1):
        print(S)
        smallest = i
        for j in range(i + 1, n):
            if S[j] < S[smallest]:
                smallest = j
        S[i], S[smallest] = S[smallest], S[i]


# selectionsort2(unlist)
# print('Sorted list', unlist)


# ==========================================================
#
# Insertion Sorting
#
# ==========================================================


# Without Swap
def insertionsort1(S):
    R = []
    while len(S) > 0:
        print(R, S)
        x = S.pop(0)
        j = len(R) - 1
        while j >= 0 and R[j] > x:
            j-= 1
        R.insert(j + 1, x)
    return R


# stlist = insertionsort1(unlist)
# print(stlist)


# With Swap (In-Place selection)
def insertionsort2(S):
    n = len(S)
    for i in range(1, n):
        print(S)
        x = S[i]
        j = i - 1
        while j >= 0 and S[j] > x:
            S[j + 1] = S[j]
            j -= 1
        S[j + 1] = x


insertionsort2(unlist)
print('Sorted list', unlist)


def is_anagram(a, b):
    a.sort()


print(is_anagram("listen", "silent"))
print(is_anagram("anagram", "nagaram"))
print(is_anagram("listen", "silence"))
print(is_anagram("anagram", "anagrams"))
