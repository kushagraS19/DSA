nums = [0,1,4,0,5,2]
l = 0

for i in nums:
    if i != 0:
        nums[l] = i
        l += 1

while l < len(nums):
    nums[l] = 0
    l += 1

print(nums)