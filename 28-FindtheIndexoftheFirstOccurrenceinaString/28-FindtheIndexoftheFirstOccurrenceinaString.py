# Last updated: 9/3/2026, 11:34:59 PM
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        r = len(needle)
4        
5        for l in range(len(haystack)):
6            if needle[:] == haystack[l:r]:
7                return l
8            if r == len(haystack):
9                break
10            r += 1
11        return -1