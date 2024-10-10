from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1

        s = 0

        while(j < len(prices)):

            if(prices[i] < prices[j]):
                s = max(prices[j] - prices[i], s)
                j+=1
            else:
                i=j
                j+=1
        return s