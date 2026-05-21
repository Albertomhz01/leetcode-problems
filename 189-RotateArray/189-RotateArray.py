# Last updated: 5/21/2026, 10:38:01 AM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        k = k % len(nums)
7        k_nums = nums[-k::]
8        rest= nums[:-k:]
9        nums[:] = k_nums + rest
10        print(nums)