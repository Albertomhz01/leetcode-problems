# Last updated: 4/16/2026, 12:55:28 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l1 = 0
        l2 = 1

        while l2 <= len(nums)-1:
            if nums[l1] == nums[l2]:
                l2 += 1
            else:
                nums[l1+1] = nums[l2]
                l1 += 1
                l2 += 1
        return l1+1