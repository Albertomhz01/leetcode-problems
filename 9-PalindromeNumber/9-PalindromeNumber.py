# Last updated: 7/30/2026, 3:58:14 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        x = str(x)
4        left = 0
5        right = len(x)-1
6
7        while left < len(x)//2:
8            if x[left] == x[right]:
9                left += 1
10                right -= 1
11            else:
12                return False
13        return True