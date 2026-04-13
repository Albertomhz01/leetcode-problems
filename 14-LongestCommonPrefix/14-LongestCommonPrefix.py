# Last updated: 4/12/2026, 10:23:16 PM
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s_min = min(strs, key=len)
        ii = 0
        jj = 0
        res = ""
        stop = False
        for s in range(len(s_min)): # len(strs[0]) = 4, flow
            # print(s_min[s]) f->l->o->w
            for ii in range(len(strs)):
                print(strs[ii][s], s_min[s])
                if strs[ii][s] != s_min[s]:
                    stop = True
                    break
                else:
                    continue
            if stop:
                break
            res += s_min[s]
        
        return res