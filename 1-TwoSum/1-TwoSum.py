# Last updated: 4/12/2026, 10:23:24 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ii = 0
        jj = ii+1
        print(len(nums))
        print(nums)

        while ii <= len(nums)-2:
            if nums[ii] + nums[jj] == target:
                return [ii, jj]
            elif jj < len(nums)-1:
                jj += 1
            else:
                ii += 1
                jj = ii+1