# Last updated: 4/12/2026, 10:23:06 PM
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        k = k - 1
        check = list()

        for ii in range(1, n+1, 1):
            if n % ii == 0:
                check.append(ii)

        if k > len(check)-1:
            return -1
        else:
            return check[k]