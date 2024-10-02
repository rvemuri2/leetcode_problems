from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:

        min_number = float('inf')
        curr = 0

        for i in nums:
            
            if(abs(i) < min_number):
                min_number = abs(i)
                curr = i
            
            if(abs(i) == min_number):
                curr = max(curr, i)

        return curr