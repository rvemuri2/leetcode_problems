from typing import List

class NumArray:
    
    def __init__(self, nums: List[int]):
        self.arr = []
        sum1 = 0
        for i in nums:
            sum1 += i
            self.arr.append(sum1)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right] - (self.arr[left - 1] if left > 0 else 0)