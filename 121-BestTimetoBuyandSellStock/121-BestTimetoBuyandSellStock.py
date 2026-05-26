# Last updated: 5/26/2026, 10:03:54 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        # Base Case:
4        if len(prices) <= 1:
5            return 0
6
7        l = 0
8        r = 1
9        diff = 0
10
11        while r < len(prices):
12            if prices[r] > prices[l]:
13                diff = max(diff, prices[r] - prices[l])
14            else: 
15                l = r
16            r += 1
17        
18        return diff