# Last updated: 7/10/2026, 2:16:02 AM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        s = "".join(char for char in s if char.isalnum())
4        s = s.lower()
5        
6        if len(s) < 1:
7            return True
8
9        left = 0
10        right = len(s) - 1
11
12        while left < (len(s))//2:
13            if s[left] == s[right]:
14                left += 1
15                right -= 1
16            else:
17                return False
18        return True