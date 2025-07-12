def containsDuplicate(nums: list[int]) -> bool:
    elements: dict[int, int] = {}
    for x in range(0, len(nums)):
        if nums[x] in elements.values():
            return True
        else:
            elements[x] = nums[x]
    return False
    # Alternative solution using set
    # return len(nums) != len(set(nums))


print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
print(containsDuplicate([1, 3, 4, 2]))
