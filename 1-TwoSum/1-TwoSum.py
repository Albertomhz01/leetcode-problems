# Last updated: 5/14/2026, 6:14:17 PM
1class Solution:
2    def longestCommonPrefix(self, strs: list[str]) -> str:
3        s_min = min(strs, key=len)
4        ii = 0
5        jj = 0
6        res = ""
7        stop = False
8        for s in range(len(s_min)): # len(strs[0]) = 4, flow
9            # print(s_min[s]) f->l->o->w
10            for ii in range(len(strs)):
11                # print(strs[ii][s], s_min[s])
12                if strs[ii][s] != s_min[s]:
13                    stop = True
14                    break
15                else:
16                    continue
17            if stop:
18                break
19            res += s_min[s]
20        
21        return res