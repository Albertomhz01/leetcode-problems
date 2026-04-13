# Last updated: 4/12/2026, 10:23:14 PM
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = None
        pre_difference = None

        for ii in range(len(nums)-2):
            l = ii+1
            r = len(nums)-1
            while l < r:
                total_sum = nums[ii] + nums[l] + nums[r]
                difference = abs(total_sum-target)
                if total_sum == target:
                    return total_sum
                elif pre_difference is None or difference < pre_difference:
                    pre_difference = difference
                    res = total_sum
                if total_sum < target:
                    l += 1
                elif total_sum > target:
                    r -= 1
        
        return res