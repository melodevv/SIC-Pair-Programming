# Pair-Programming
def multiway_merge(lists):
    merged = []
    indices = [0] * len(lists)
    while True:
        smallest = None
        smallest_idx = None
        for l, lst in enumerate(lists):
            if indices[l] < len(lst):
                if smallest is None or lst[indices[l]] < smallest:
                    smallest = lst[indices[l]]
                    smallest_idx = l
        if smallest is None:
            break
        merged.append(smallest)
        indices[smallest_idx] += 1
    sorted_lst = sorted(merged)
    return sorted_lst


N = int(input("Input the number of lists: "))
list_of_nums = []
for i in range(N):
    nums = list(map(int, input('Input a list of numbers: ').split()))
    print(nums)
    list_of_nums.append(nums)
sorted_list = multiway_merge(list_of_nums)
print('Merged into:', sorted_list)
