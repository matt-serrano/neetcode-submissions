class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
          

'''
def productExceptSelf(nums):
    nums2 = []

    product = 1
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if (j == i):
                continue
            product = product * nums[j]

        nums2.append(product)
        product = 1

    return nums2

'''