from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0

        while(nums != [0] * len(nums)):

            least = float('inf')
            for i in nums:
                if i != 0 and i < least:
                    least = i

            for i in range(len(nums)):

                if(nums[i] != 0):
                    nums[i] -= least
    
            operations += 1
        return operations