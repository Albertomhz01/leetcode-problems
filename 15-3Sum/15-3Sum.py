# Last updated: 7/30/2026, 3:49:18 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        
4        nums.sort()
5        res = []
6
7        ii = 0
8        while ii < len(nums) - 2:
9
10            # skip duplicate ii
11            if ii > 0 and nums[ii] == nums[ii - 1]:
12                ii += 1
13                continue
14
15            l = ii + 1
16            r = len(nums) - 1
17
18            while l < r:
19                total_sum = nums[ii] + nums[l] + nums[r]
20
21                if total_sum == 0:
22                    res.append([nums[ii], nums[l], nums[r]])
23
24                    l += 1
25                    r -= 1
26
27                    # skip duplicates for l
28                    while l < r and nums[l] == nums[l - 1]:
29                        l += 1
30
31                    # skip duplicates for r
32                    while l < r and nums[r] == nums[r + 1]:
33                        r -= 1
34
35                elif total_sum < 0:
36                    l += 1
37                else:
38                    r -= 1
39
40            ii += 1
41
42        return res