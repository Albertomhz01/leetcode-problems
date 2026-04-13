# Last updated: 4/12/2026, 10:23:22 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)

        if not s:
            value = 0
        else:
            value = 1
        
        for ii in range(len(s)):
            ptr = list(s[ii])
            count = 1
            for kk in range(ii+1, len(s)):
                if s[kk] not in ptr:
                    ptr.append(s[kk])
                    count += 1
                    if value < count:
                        value = count
                else:
                    ptr = []
                    break

        return value