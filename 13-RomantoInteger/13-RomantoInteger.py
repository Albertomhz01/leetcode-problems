# Last updated: 7/30/2026, 3:50:41 PM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        roman_val = {"I": 1, "V": 5, "X": 10, 
4        "L": 50, "C": 100, "D": 500, "M": 1000}
5
6        res = []
7        total = 0
8
9        ii = 0
10        while ii < len(s):
11            if ii < len(s)-1 and roman_val[s[ii]] < roman_val[s[ii+1]]:
12                total += roman_val[s[ii+1]] - roman_val[s[ii]]
13                ii += 2
14            else:
15                total += roman_val[s[ii]]
16                ii += 1
17        
18        return total