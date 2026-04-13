# Last updated: 4/12/2026, 10:23:13 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for ii in nums1[::-1]:
            if len(nums1) == m:
                break
            if ii == 0:
                nums1.remove(ii)
            elif ii != 0:
                break
            
        for ii in nums2[::-1]:
            if len(nums2) == n:
                break
            if ii == 0:
                nums2.remove(ii)
            elif ii != 0:
                break
        
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        