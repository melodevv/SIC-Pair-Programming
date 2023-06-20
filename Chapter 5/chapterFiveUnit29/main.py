def find_kth_largest_sort(numb, k):
    numb.sort(reverse=True)
    return numb[k - 1]


def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] >= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


def quick_sort(numbers, low, high, k):
    if low <= high:
        pivot_point = partition(numbers, low, high)

        if pivot_point == k - 1:
            return numbers[pivot_point]
        elif pivot_point > k - 1:
            return quick_sort(numbers, low, pivot_point - 1, k)
        else:
            return quick_sort(numbers, pivot_point + 1, high, k)


def find_kth_largest_partition(num, k):
    return quick_sort(num, 0, len(num) - 1, k)


# Example usage:
nums = [3, 5, 2, 9, 10]
k = 3

kth_largest_sort = find_kth_largest_sort(nums, k)
kth_largest_partition = find_kth_largest_partition(nums, k)

print("Kth largest element (Sort Method):", kth_largest_sort)
print("Kth largest element (Partition Method):", kth_largest_partition)
