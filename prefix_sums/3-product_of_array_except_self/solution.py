from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        pre = 1

        for i in range(len(nums)):
            arr[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            arr[i] *= post
            post *= nums[i]
        
        return arr