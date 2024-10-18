from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        h = {}
        sum1 = 0
        h[0] = -1

        for i in range(len(nums)):

            sum1 += nums[i]
            r = sum1 % k

            if(r not in h):
                h[r] = i

            elif(i - h[r] > 1):
                return True

        return False