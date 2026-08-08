# Last updated: 8/7/2026, 9:59:56 PM
1from collections import deque
2class Solution:
3    def numIslands(self, grid: List[List[str]]) -> int:
4        if not grid:
5            return
6
7        rows, cols = len(grid), len(grid[0])
8        islands = 0
9        visit = set()
10
11        def dfs(r, c):
12            if (r not in range(rows) or
13                c not in range(cols) or
14                grid[r][c] == "0" or
15                (r, c) in visit):
16                return
17
18            visit.add((r, c))
19
20            dfs(r + 1, c)
21            dfs(r - 1, c)
22            dfs(r, c + 1)
23            dfs(r, c - 1)
24
25        for r in range(rows):
26            for c in range(cols):
27                if grid[r][c] == "1" and (r, c) not in visit:
28                    dfs(r, c)
29                    islands += 1
30        return islands