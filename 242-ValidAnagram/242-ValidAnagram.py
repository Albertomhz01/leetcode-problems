# Last updated: 8/10/2026, 7:41:45 PM
1from collections import Counter
2class Solution:
3    def isAnagram(self, s: str, t: str) -> bool:
4        map_s = Counter(s)
5        map_t = Counter(t)
6
7        if map_s == map_t:
8            return True
9        else:
10            return False
11        