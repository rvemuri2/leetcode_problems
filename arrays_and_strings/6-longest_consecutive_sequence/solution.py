from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        count = 1
        temp = 0

        nums1 = set(nums)

        if(len(nums1) == 0):
            return 0

        for i in nums1:

            temp = i
            if(temp - 1 not in nums1):
                curr_streak = 1
                while(temp + 1 in nums1):
                    curr_streak += 1
                    temp += 1     
                count = max(curr_streak, count)
        
        return count