def maximum_subarray(arr):
    max_sum = float('-inf')  # set to negative infinity
    current_sum = 0
    start_index = 0
    end_index = 0
    current_start_index = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = current_start_index
            end_index = i

        if current_sum < 0:
            current_sum = 0
            current_start_index = i + 1

    return sum(arr[start_index:end_index + 1])


S = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
M = maximum_subarray(S)
print(M)
