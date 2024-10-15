from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        length = float("inf")
        sum1 = 0

        for i in range(len(nums)):
            sum1 += nums[i]
            while(sum1 >= target):
                length = min(length, i - l + 1)
                sum1 -= nums[l]
                l += 1
        
        return 0 if length == float('inf') else length
    
