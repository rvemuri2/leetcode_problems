import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        res = float('infinity')

        while(l <= r):
            k = (l + r) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i / k)
            
            if(hours <= h):
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res