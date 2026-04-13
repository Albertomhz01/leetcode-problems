# Last updated: 4/12/2026, 10:23:09 PM
class Solution:
    memo = {}
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 1:
            return n
        elif n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
            return self.memo[n]

        return self.memo[n]