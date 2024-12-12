from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        right = sum(weights)
        left = max(weights)
        res = float('infinity')


        def canShip(cap):
            ships = 1
            currCap = cap
            for w in weights:
                if(currCap - w < 0):
                    ships += 1
                    currCap = cap
                currCap -= w
            
            if(ships <= days):
                return True
            else:
                return False

        while(left <= right):
            mid = (right + left) // 2
            if(canShip(mid)):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return res