# Last updated: 7/27/2026, 8:05:33 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()
        
        if len(s) < 1:
            return True

        left = 0
        right = len(s) - 1

        while left < (len(s))//2:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True