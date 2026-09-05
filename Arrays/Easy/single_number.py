def single_number(nums:list[int]):
    for i in nums:
        if nums.count(i) == 1:
            print(i)

single_number([1,1,2,2,3,3,7])