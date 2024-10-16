from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)
        prevSum = 0

        for i in range(len(nums)):

            rightSum = total - nums[i] - prevSum
            
            if(prevSum == rightSum):
                return i
            
            prevSum += nums[i] 
        
        return -1