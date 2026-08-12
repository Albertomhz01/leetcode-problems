# Last updated: 8/12/2026, 2:33:13 PM
1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        s = s.rstrip()
4        res = list()
5        for word in s[::-1]:
6            if word == " ":
7                break
8            else:
9                print(word)
10                res.append(word)
11        return len(res)
12