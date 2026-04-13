# Last updated: 4/12/2026, 10:23:21 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums3 = nums1 + nums2
        nums3 = sorted(nums3)
        print(nums3)

        if len(nums3)%2 == 0:
            M = int(len(nums3)/2)
            M2 = int((len(nums3)/2)+1)
            Median = (nums3[M-1] + nums3[M2-1])/2
            return Median
        else:
            M = int((len(nums3)+1)/2)
            Median = nums3[M-1]
            return Median