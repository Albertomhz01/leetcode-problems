# Last updated: 4/12/2026, 10:23:19 PM
from collections import deque
class Solution:
    def reverse(self, x: int) -> int:
        # Teste Case if is 0
        if x == 0:
            return 0
        x = str(x)
        x = list(x)
        res = deque()

        if x[0] == "-":
            for c in x[1:][::-1]:
                res.append(c)
            s = ''.join(str(x) for x in res)
            s = s.lstrip("0")
            s = "-" + s
            if int(s) < -2**31 or int(s) > (2**31)-1:
                return 0
            return int(s)
        else:
            for c in x[:][::-1]:
                res.append(c)
            s = ''.join(str(x) for x in res)
            s = s.lstrip("0")
            if int(s) < -2**31 or int(s) > (2**31)-1:
                return 0
            return int(s)