# Last updated: 7/10/2026, 1:53:04 AM
1class Solution:
2    def hIndex(self, citations: List[int]) -> int:
3        if len(citations) == 1 and citations[0] == 0:
4            return 0
5        elif len(citations) == 1:
6            return 1
7
8        citations = sorted(citations)
9        
10        for ii, n in enumerate(citations[::-1]):
11            if n >= ii+1:
12                continue
13            else:
14                return ii
15
16        return ii+1