# Last updated: 8/16/2026, 11:05:02 AM
1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        res = []
4        left, right = 0, len(matrix[0])
5        top, bottom = 0, len(matrix)
6
7        while left < right and top < bottom:
8            # get every ii inthe top row
9            for ii in range(left, right):
10                res.append(matrix[top][ii])
11            top += 1
12            # get every ii in the right col
13            for ii in range(top, bottom):
14                res.append(matrix[ii][right-1])
15            right -= 1
16
17            if not (left < right and top < bottom):
18                break
19
20            # get every ii in the bottom row
21            for ii in range(right-1, left-1, -1):
22                res.append(matrix[bottom-1][ii])
23            bottom -= 1
24            # get every ii in the left col
25            for ii in range(bottom-1, top-1, -1):
26                res.append(matrix[ii][left])
27            left += 1
28        
29        return res