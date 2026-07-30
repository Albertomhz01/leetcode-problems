# Last updated: 7/30/2026, 3:52:23 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        if not s:
4            return None
5        
6        start = 0
7        end = 0
8        
9        def expand(l, r):
10            while l >= 0 and r < len(s) and s[l] == s[r]:
11                l -= 1
12                r += 1
13            return l + 1, r - 1
14        
15        for i in range(len(s)):
16            # odd length
17            l1, r1 = expand(i, i)
18            # even length
19            l2, r2 = expand(i, i + 1)
20            
21            if r1 - l1 > end - start:
22                start, end = l1, r1
23            if r2 - l2 > end - start:
24                start, end = l2, r2
25        
26        return s[start:end + 1]