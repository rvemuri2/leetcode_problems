from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0

        stock = 0

        for i in range(len(prices)):

            if(prices[i] > prices[l]):
                stock = max(stock, prices[i] - prices[l])
            else:
                l=i
            
        return stock