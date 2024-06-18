class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      
        pr=0
        buy=prices[0]
        for i in range(len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            elif prices[i]-buy>pr:
                pr=prices[i]-buy
        return pr
        