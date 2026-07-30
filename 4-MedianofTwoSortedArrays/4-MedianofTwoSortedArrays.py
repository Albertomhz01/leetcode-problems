# Last updated: 7/30/2026, 3:59:39 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3
4        nums3 = nums1 + nums2
5        nums3 = sorted(nums3)
6        print(nums3)
7
8        if len(nums3)%2 == 0:
9            M = int(len(nums3)/2)
10            M2 = int((len(nums3)/2)+1)
11            Median = (nums3[M-1] + nums3[M2-1])/2
12            return Median
13        else:
14            M = int((len(nums3)+1)/2)
15            Median = nums3[M-1]
16            return Median