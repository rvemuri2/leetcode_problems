from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        h = {}

        for i in range(len(nums)):
            if(target - nums[i] in h):
                return [i, h[target - nums[i]]]

            else:
                h[nums[i]] = i 
        