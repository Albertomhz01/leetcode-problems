# Last updated: 9/5/2026, 1:19:57 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        map = {}
4
5        for ii, n in enumerate(numbers):
6            diff = target - n
7            if diff in map:
8                return [map[diff]+1, ii+1]
9            map[n] = ii
10        return
11        