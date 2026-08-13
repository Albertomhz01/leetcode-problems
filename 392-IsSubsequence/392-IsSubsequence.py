# Last updated: 8/13/2026, 1:06:19 AM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        right_s = len(s)-1
4        right_t = len(t)-1
5        
6        if right_s == -1:
7            return True
8        elif right_t == -1:
9            return False
10
11        print(right_s, right_t)
12
13        while right_t >= 0:
14            if t[right_t] == s[right_s]:
15                right_s -= 1
16                print(right_s)
17            right_t -= 1
18
19        if right_s <= -1:
20            return True
21        else:
22            return False