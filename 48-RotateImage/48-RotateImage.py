# Last updated: 8/16/2026, 2:07:12 PM
1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        res = [row[:] for row in matrix]
7        rows, cols = len(matrix), len(matrix[0])
8    
9        for r in reversed(range(rows)):
10            for c in range(cols):
11                matrix[r][c] = res[c][r]
12
13        for ii in range(len(matrix)):
14            matrix[ii].reverse()