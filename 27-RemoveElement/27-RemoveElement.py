# Last updated: 4/12/2026, 10:23:14 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for ii in range(len(nums)):
            if nums[ii] != val:
                nums[k] = nums[ii]
                k += 1

        return k