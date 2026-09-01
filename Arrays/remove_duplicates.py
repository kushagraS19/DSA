def remove_duplicates(arr : list[int]):
    l = 0

    for r in range(1,len(arr)):
        if arr[r] != arr[l]:
            l += 1
            arr[l] = arr[r]

    return l + 1

print(remove_duplicates([0,0,3,3,4,5,6]))