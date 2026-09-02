# Rotate array by one -->

"""
arr = [1,2,3,4,5]
l = 0
r = 1

for i in range(len(arr)-1):
    arr[l],arr[r] = arr[r],arr[l]
    r += 1
    l += 1

print(arr)

"""

# Rotate array by k places -->

def rotate_array (nums : list[int], k : int):
    n = len(nums)
    if k >= n:
        k = k % n

    nums.reverse()

    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

nums = [1,2,3,4,5,6]
rotate_array(nums, 6)
print(nums)