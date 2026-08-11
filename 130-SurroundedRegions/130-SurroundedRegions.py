# Last updated: 8/10/2026, 11:18:02 PM
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
21            print(visit)
22
23            dfs(r + 1, c)
24            dfs(r - 1, c)
25            dfs(r, c + 1)
26            dfs(r, c - 1)
27
28        # for r in range(rows):
29        #     for c in range(cols):
30        #         if (board[r][c] == "O" and (r, c) not in visit and
31        #         r == 0 or r == rows-1 or
32        #         c == 0 or c == rows-1):
33
34        for r in range(rows):
35            for c in range(cols):
36                if (board[r][c] == "O" and
37                (r, c) not in visit and
38                (r == 0 or r == rows - 1 or
39                c == 0 or c == cols - 1)):
40                    dfs(r, c)
41
42        for r in range(rows):
43            for c in range(cols):
44                if board[r][c] == "O":
45                    board[r][c] = "X"
46        
47        for r in range(rows):
48            for c in range(cols):
49                if board[r][c] == "T":
50                    board[r][c] = "O"