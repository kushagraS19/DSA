arr = [1,2,3,4,5]
l = 0
r = 1

for i in range(len(arr)-1):
    arr[l],arr[r] = arr[r],arr[l]
    r += 1
    l += 1

print(arr)