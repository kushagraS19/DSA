def missing_number(arr : list[int]):
    n = len(arr)

    expected_sum = n * (n+1) // 2
    actual = sum(arr)

    missing = expected_sum - actual

    return missing

print(missing_number([0,1,2,4,5]))