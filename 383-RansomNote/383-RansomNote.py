# Last updated: 7/27/2026, 8:02:51 PM
1from collections import defaultdict
2class Solution:
3    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
4        counter = defaultdict(int)
5
6        for word in magazine:
7            counter[word] += 1
8
9        for ii in ransomNote:
10            if ii in counter and counter[ii] > 0:
11                counter[ii] -= 1
12            else:
13                return False
14        
15        return True
16        