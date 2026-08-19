# Last updated: 8/19/2026, 12:07:03 AM
1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        map = {}
4        s_list = s.split()
5        pattern_list = list()
6        kk = 0
7
8        for word in pattern:
9            pattern_list.append(word)
10
11        if len(pattern_list) > len(s_list):
12            return False
13
14        for ii in pattern:
15            map[ii] = s_list[kk]
16            print(map[ii], s_list[kk])
17            kk += 1
18
19        has_duplicates = len(map) != len(set(map.values()))
20        if has_duplicates == True:
21            return False
22
23        reword = ""
24        for ii in pattern_list:
25            reword += " "
26            reword += map[ii]
27
28        reword = reword.strip()
29        if reword == s:
30            return True
31        else:
32            return False