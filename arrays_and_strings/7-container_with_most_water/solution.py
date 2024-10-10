from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        i = 0
        j = len(height) - 1

        res = 0

        while(i < j):

            if(height[i] < height[j]):
                prod = height[i] * (j - i)
                res = max(res, prod)
                i += 1
            else:
                prod = height[j] * (j - i)
                res = max(res, prod)
                j -= 1
            
        return res