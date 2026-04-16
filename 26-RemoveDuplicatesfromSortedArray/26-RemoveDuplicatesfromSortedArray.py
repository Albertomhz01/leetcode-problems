# Last updated: 4/15/2026, 9:18:16 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        l1 = 0
4        l2 = 1
5        print(len(nums)-1)
6        print(nums)
7
8        while l2 <= len(nums)-1:
9            if nums[l1] == nums[l2]:
10                print(f"same numbers: {nums[l1]}, {nums[l2]}")
11                l2 += 1
12            else:
13                nums[l1+1] = nums[l2]
14                l1 += 1
15                l2 += 1
16        return l1+1