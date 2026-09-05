def is_sorted (arr : list[int]) -> bool:
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False

    return True

print(is_sorted([1,4,40,8]))