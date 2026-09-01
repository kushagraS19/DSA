def find_second_largest (arr : list[int]) -> int :
    minus_inf = float("-inf")
    largest = minus_inf

    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i

        elif largest > i > second_largest:
            second_largest = i

    if second_largest == minus_inf:
            return -1

    return second_largest

print(find_second_largest([1,1,1,1]))