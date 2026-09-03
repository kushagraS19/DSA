nums = [1,1,0,0,1]

count = 0
max_n = 0 

for num in nums:
    if num == 1:
        count += 1
        max_n = max(max_n, count)
    else :
        count = 0

print(max_n)