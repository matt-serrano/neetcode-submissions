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

#make a hashmap
#enumerate the list with a for loop (grab values and index)
#create the compliment number
#if the compliment number is in the hashmap, return the index, and the current index
#otherwise, store the compliment number, along with the index, in the hashmap 