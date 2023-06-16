# # ========================================
# #
# #               Merge Sort
# #            Divide and Conquer
# #
# # ========================================
#
# def mergesort1(S):
#     n = len(S)
#     if n > 1:
#         print(S)
#         mid = n // 2
#         L, R = S[:mid], S[mid:]
#         mergesort1(L)
#         mergesort1(R)
#         merge1(S, L, R)
#
#
# def merge1(S, L, R):
#     k = 0               # Indexer
#     while len(L) > 0 and len(R) > 0:
#         if L[0] <= R[0]:
#             S[k] = L.pop(0)
#         else:
#             S[k] = R.pop(0)
#         k += 1          # Increase Indexer
#     while len(L) != 0:
#         S[k] = L.pop(0)
#         k += 1
#     while len(R) != 0:
#         S[k] = R.pop(0)
#         k += 1
#
#
# S = [27, 10, 12, 20, 25, 13, 15, 22]
# # mergesort1(S)
# # print(S)
#
#
# # ========================================
# #
# #               Merge Sort
# #          Enhanced Merge Sort
# #
# # ========================================
#
#
# def mergesort2(S, low, high):
#     print('mergesort2 executed: ')
#     if low < high:
#         print(S)
#         mid = (low + high) // 2
#         mergesort2(S, low, mid)
#         mergesort2(S, mid + 1, high)
#         merge2(S, low, mid, high)
#
#
# def merge2(S, low, mid, high):
#     R = []
#     i, j = low, mid + 1
#     while i <= mid and j <= high:
#         if S[i] < S[j]:
#             R.append(S[i]); i += 1
#         else:
#             R.append(S[j]); j += 1
#     if i > mid:
#         for k in range(j, high + 1):
#             R.append(S[j])
#     else:
#         for k in range(i, mid + 1):
#             R.append(S[i])
#     for k in range(len(R)):
#         S[low + k] = R[k]
#
#
# mergesort2(S, 0, len(S) - 1)
# print(S)

def multiway_merge(nums):
    R = []
    rlist = []
    k = 0
    while len(nums) > 0:
        for row in range(len(nums)):
            for col in range(len(nums[row]) - 1):
                if row != (len(nums) - 1):
                    if nums[row][col] < nums[row + 1][col]:
                        R.append(nums[row].pop(col))
                    else:
                        R.append(nums[row + 1].pop(col))

                else:
                    if nums[row - 1][col] < nums[row][col]:
                        R.append(nums[row - 1].pop(col))
                    else:
                        R.append(nums[row].pop(col))
    return R


# N = int(input("Input the number of list: "))
list_of_nums = [
    [1, 5],
    [2, 6],
    [3, 4, 7]
]
# for i in range(N):
#     nums = list(map(int, input("Input a list of numbers: ").split()))
#     print(nums)
#     list_of_nums.append(nums)
sorted = multiway_merge(list_of_nums)
print("Merged into : ", sorted)
