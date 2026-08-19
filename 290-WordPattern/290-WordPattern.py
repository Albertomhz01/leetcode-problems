# Last updated: 8/19/2026, 12:10:50 AM
1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        s_list = s.split()
4
5        if len(pattern) != len(s_list):
6            return False
7
8        map = {}
9        used = set()
10
11        for ii in range(len(pattern)):
12            char = pattern[ii]
13            word = s_list[ii]
14
15            if char in map:
16                if map[char] != word:
17                    return False
18            else:
19                if word in used:
20                    return False
21
22                map[char] = word
23                used.add(word)
24
25        return True