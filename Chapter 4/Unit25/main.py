def search_insert_position(nums, x):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    if x > high:
        return high + 1

    return high


nums = [10, 20, 40, 50, 60, 80]
x = int(input("Input a number to insert: "))
pos = search_insert_position(nums, x)
print(f"{x} should be inserted at position {pos}.")
nums.insert(pos, x)
print(nums)
