# Last updated: 8/10/2026, 11:18:49 PM
1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        if not board: return
7
8        rows, cols = len(board), len(board[0])
9        visit = set()
10        islands = 0
11
12        def dfs(r, c):
13            if (r not in range(rows) or
14                c not in range(cols) or
15                board[r][c] == "X" or
16                (r, c) in visit):
17                return
18            
19            board[r][c] = "T"
20            visit.add((r, c))
21
22            dfs(r + 1, c)
23            dfs(r - 1, c)
24            dfs(r, c + 1)
25            dfs(r, c - 1)
26
27        for r in range(rows):
28            for c in range(cols):
29                if (board[r][c] == "O" and
30                (r, c) not in visit and
31                (r == 0 or r == rows - 1 or
32                c == 0 or c == cols - 1)):
33                    dfs(r, c)
34
35        for r in range(rows):
36            for c in range(cols):
37                if board[r][c] == "O":
38                    board[r][c] = "X"
39        
40        for r in range(rows):
41            for c in range(cols):
42                if board[r][c] == "T":
43                    board[r][c] = "O"