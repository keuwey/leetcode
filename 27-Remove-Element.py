def removeElement(nums: list[int], val: int) -> int:
    i: int = len(nums) - 1
    while i >= 0:
        if nums[i] == val:  # [nums.pop(i) if nums[i] == val else ""]
            nums.pop(i)
        i -= 1

    return len(nums)


print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
