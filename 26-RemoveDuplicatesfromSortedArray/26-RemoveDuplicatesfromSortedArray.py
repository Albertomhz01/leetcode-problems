# Last updated: 4/15/2026, 9:19:03 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        l1 = 0
4        l2 = 1
5
6        while l2 <= len(nums)-1:
7            if nums[l1] == nums[l2]:
8                l2 += 1
9            else:
10                nums[l1+1] = nums[l2]
11                l1 += 1
12                l2 += 1
13        return l1+1