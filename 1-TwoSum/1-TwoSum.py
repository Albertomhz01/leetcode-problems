# Last updated: 4/30/2026, 9:50:18 PM
1class Solution(object):
2    def twoSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        prevMap = {} # val : index
9
10        for ii, n in enumerate(nums):
11            diff = target - n
12            if diff in prevMap:
13                return [prevMap[diff], ii]
14            prevMap[n] = ii
15        return
16        