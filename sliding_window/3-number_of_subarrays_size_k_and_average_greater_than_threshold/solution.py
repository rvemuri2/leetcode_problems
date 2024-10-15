from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        l = 0
        count = 0
        sum1 = 0

        for i in range(len(arr)):

            sum1 += arr[i]

            if(i - l + 1 > k):
                sum1 -= arr[l]
                l+=1
            
            if(i - l + 1 == k):
                avg = sum1/k
                if(avg >= threshold):
                    count+=1
                
        
        return count