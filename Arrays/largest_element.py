# Find Largest element from an array -->

def find_largest (arr : list[int]):
    largest = float("-inf")

    for i in arr:
        if i > largest:
            largest = i

    return largest

num = find_largest([6,5,47,4])
print(num)