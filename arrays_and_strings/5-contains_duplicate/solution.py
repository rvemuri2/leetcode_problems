class Solution(object):
    def containsDuplicate(self, nums):
        
        l = set(nums)
        if(len(nums) == len(l)):
            return False
        else:
            return True