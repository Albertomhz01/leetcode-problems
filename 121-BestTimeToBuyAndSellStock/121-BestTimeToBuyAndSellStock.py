# Last updated: 5/26/2026, 10:05:43 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Base Case:
        if len(prices) <= 1:
            return 0

        l = 0
        r = 1
        diff = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                diff = max(diff, prices[r] - prices[l])
            else: 
                l = r
            r += 1
        
        return diff