from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        l = 0
        h = set()

        for i in range(len(nums)):
            if(i - l > k):
                h.remove(nums[l])
                l += 1
            
            if(nums[i] in h):
                return True

            h.add(nums[i])

        return False