def adding(nums):
    if not nums:
        return 0
    return nums.pop() + adding(nums)

print(adding([1,2,3,4,5]))