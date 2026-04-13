# Last updated: 4/12/2026, 10:23:15 PM
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        res = []

        ii = 0
        while ii < len(nums) - 2:

            # skip duplicate ii
            if ii > 0 and nums[ii] == nums[ii - 1]:
                ii += 1
                continue

            l = ii + 1
            r = len(nums) - 1

            while l < r:
                total_sum = nums[ii] + nums[l] + nums[r]

                if total_sum == 0:
                    res.append([nums[ii], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # skip duplicates for l
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # skip duplicates for r
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif total_sum < 0:
                    l += 1
                else:
                    r -= 1

            ii += 1

        return res
