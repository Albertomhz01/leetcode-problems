# Last updated: 7/30/2026, 3:48:42 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        area = 0
4        ii = 0
5        jj = len(height)-1
6
7        while ii < jj:
8            if height[ii] < height[jj]:
9                if area < height[ii]*(jj-ii):
10                    area = height[ii]*(jj-ii)
11                ii += 1
12            else:
13                if area < height[jj]*(jj-ii):
14                    area = height[jj]*(jj-ii)
15                jj -= 1
16
17        return area