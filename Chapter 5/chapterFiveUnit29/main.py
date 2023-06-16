from random import randint
# ========================================
#
#               Quick Sort
#           Divide and Conquer
#
# ========================================

def partition1(S, low, high):
    pivot = S[low]
    left, right = low + 1, high
    while left < right:
        print(S)

        # working on the left side
        # starting from the leftmost
        while left <= right and S[left] <= pivot:
            left += 1

        # working on the right side
        # starting from the rightmost
        while left <= right and S[right] >= pivot:
            right -= 1

        # Perform the swap of elements on the right and left
        if left < right:
            S[left], S[right] = S[right], S[left]
    pivotpoint = right
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    return pivotpoint


def quicksort1(S, low, high):
    if low < high:
        print(S)
        pivotpoint = partition1(S, low, high)
        quicksort1(S, low, pivotpoint -1)
        quicksort1(S, pivotpoint +1, high)


def partition2(S, low, high):
    rand = randint(low, high)

    # first element changed to a random element
    S[low], S[rand] = S[rand], S[low]
    pivot, left, right = S[low], low, high
    print(S, left, right, "pivot = ", pivot)

    while left < right:
        while left < high and S[left] <= pivot:
            left += 1
        while right > low and pivot <= S[right]:
            right -= 1
        if left < right:
            S[left], S[right] = S[right], S[left]
    S[low], S[right] = S[right], S[low]
    return right


def quicksort2(S, low, high):
    if low < high:
        pivotpoint = partition2(S, low, high)
        quicksort2(S, low, pivotpoint - 1)
        quicksort2(S, pivotpoint + 1, high)


S = [15, 10, 12, 20, 25, 13, 22]
# S = [25, 22, 20, 15, 13, 12, 10]

#
# First element is used a pivot
#
# quicksort1(S, 0, len(S) - 1)
# print(S)

#
# Pivot selected at random
#
# quicksort2(S, 0, len(S) - 1)
# print(S)


# ========================================
#
#               Quick Sort
#                Pop Quiz
#
# ========================================
partition1(S, 0, len(S) - 1)
print('answer :', S)
