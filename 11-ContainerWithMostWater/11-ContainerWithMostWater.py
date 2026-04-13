# Last updated: 4/12/2026, 10:23:18 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        ii = 0
        jj = len(height)-1

        while ii < jj:
            if height[ii] < height[jj]:
                if area < height[ii]*(jj-ii):
                    area = height[ii]*(jj-ii)
                ii += 1
            else:
                if area < height[jj]*(jj-ii):
                    area = height[jj]*(jj-ii)
                jj -= 1

        return area