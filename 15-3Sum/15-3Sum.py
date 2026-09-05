# Last updated: 9/5/2026, 3:35:24 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums = sorted(nums)
4        res = list()
5
6        for ii in range(len(nums)):
7            if ii > 0 and nums[ii] == nums[ii - 1]:
8                continue
9            l = ii + 1
10            r = len(nums)-1
11            while l < r:
12                total = nums[ii] + nums[l] + nums[r]
13                if total == 0:
14                    res.append([nums[ii], nums[l], nums[r]])
15                    l += 1
16                    r -= 1
17
18                    while l < r and nums[l] == nums[l - 1]:
19                        l += 1
20
21                    while l < r and nums[r] == nums[r + 1]:
22                        r -= 1
23                elif total < 0:
24                    l += 1
25                else:
26                    r -= 1
27        
28        return res