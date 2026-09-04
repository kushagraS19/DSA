nums = [10, 5, 2, 7, 1, 9]
k = 15

prefix_sum = 0
max_len = 0
seen = {0: -1}

for i in range(len(nums)):
    prefix_sum += nums[i]

    if prefix_sum - k in seen:
        max_len = max(max_len, i - seen[prefix_sum - k])

    if prefix_sum not in seen:
        seen[prefix_sum] = i

print(max_len)

class Solution:
    def longestSubarray(self, nums, k):
        pre_sum = 0
        max_len = 0
        seen = {0 : -1}

        for i in range(len(nums)):
            pre_sum += nums[i]

            if pre_sum - k in seen:
                max_len = max(max_len, i - seen[pre_sum - k])

            if pre_sum not in seen:
                seen[pre_sum] = i

        return max_len

s = Solution()
print(s.longestSubarray([10, 5, 2, 7, 1, 9],15))