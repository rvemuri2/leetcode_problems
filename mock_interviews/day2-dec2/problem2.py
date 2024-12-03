from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        c = Counter(nums)

        for i in c.values():

            if(i % 2 == 1):
                return False
        
        return True