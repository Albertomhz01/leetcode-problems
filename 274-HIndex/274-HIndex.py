# Last updated: 7/27/2026, 8:05:29 PM
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1 and citations[0] == 0:
            return 0
        elif len(citations) == 1:
            return 1

        citations = sorted(citations)
        
        for ii, n in enumerate(citations[::-1]):
            if n >= ii+1:
                continue
            else:
                return ii

        return ii+1