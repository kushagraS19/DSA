def linear_search(nums : list[int], target : int) -> int :

    for i in range(len(nums)-1):
        if nums[i] == target:
            return i

    return -1

nums = [1,2,3,4,5,7]
result = linear_search(nums, 9)
print(result)