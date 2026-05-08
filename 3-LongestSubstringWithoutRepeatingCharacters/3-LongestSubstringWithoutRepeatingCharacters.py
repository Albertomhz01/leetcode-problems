# Last updated: 5/7/2026, 11:15:53 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        charSet = set()
4        left = 0
5        res = 0
6
7        for right in range(len(s)):
8            while s[right] in charSet:
9                charSet.remove(s[left])
10                left += 1
11
12            charSet.add(s[right])
13            res = max(res, right - left + 1)
14
15        return res