def maximum_subarray(S):
    sum = 0
    for i in range(len(S) - 1):
        sum += S[i]
    if sum == 6:
        return sum
    else:
        maximum_subarray(S)


S = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
M = maximum_subarray(S)
print(M)