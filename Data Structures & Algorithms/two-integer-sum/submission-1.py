class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, x in enumerate(nums):
            compliment = target - x

            if compliment in num_map:
                return [num_map[compliment], i]
            else:
                num_map[x] = i
        
        return []