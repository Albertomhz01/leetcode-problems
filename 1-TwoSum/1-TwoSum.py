# Last updated: 4/30/2026, 11:33:59 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        prevMap = {} # val : index
4
5        for ii, n in enumerate(nums):
6            diff = target - n
7            if diff in prevMap:
8                return [prevMap[diff], ii]
9            prevMap[n] = ii
10        return