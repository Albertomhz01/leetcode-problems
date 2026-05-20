# Last updated: 5/20/2026, 12:13:58 AM
1from collections import defaultdict
2class Solution:
3    def majorityElement(self, nums: List[int]) -> int:
4        map = defaultdict(int)
5
6        for item in nums:
7            map[item] += 1
8
9        return max(map, key=map.get)