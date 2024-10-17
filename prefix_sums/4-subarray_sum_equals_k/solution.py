from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum1 = 0
        res = 0

        h = {}
        h[0] = 1

        for i in range(len(nums)):
            sum1 += nums[i]
            if(sum1 - k in h):
                res += h.get(sum1 - k, 0)
            h[sum1] = h.get(sum1, 0) + 1
        
        return res