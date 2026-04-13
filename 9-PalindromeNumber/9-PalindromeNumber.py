# Last updated: 4/12/2026, 10:23:18 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x = list(str(x))

        if x[:] == x[::-1]:
            return True
        else:
            return False