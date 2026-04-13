# Last updated: 4/12/2026, 10:23:17 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_val = {"I": 1, "V": 5, "X": 10, 
        "L": 50, "C": 100, "D": 500, "M": 1000}

        res = []
        total = 0

        ii = 0
        while ii < len(s):
            if ii < len(s)-1 and roman_val[s[ii]] < roman_val[s[ii+1]]:
                total += roman_val[s[ii+1]] - roman_val[s[ii]]
                ii += 2
            else:
                total += roman_val[s[ii]]
                ii += 1
        
        return total