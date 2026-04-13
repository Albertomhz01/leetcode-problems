# Last updated: 4/12/2026, 10:23:10 PM
import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        w = int(math.sqrt(area))
    
        while area % w != 0:
            w = w-1

        l = area // w
        return [l, w]