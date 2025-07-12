def removeDuplicates(nums: list[int]) -> int:
    index: int = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[index]:
            index += 1
            nums[index] = nums[i]
    return index + 1


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
