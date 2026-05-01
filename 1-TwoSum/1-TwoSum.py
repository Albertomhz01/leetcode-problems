# Last updated: 4/30/2026, 11:15:23 PM
1from collections import deque
2class Solution:
3    def numIslands(self, grid: List[List[str]]) -> int:
4        if not grid:
5            return 0
6
7        rows, cols = len(grid), len(grid[0])
8        visit = set()
9        islands = 0
10
11        def bfs(r, c):
12            q = deque()
13            visit.add((r, c))
14            q.append((r, c))
15
16            while q:
17                row, col = q.popleft()
18                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
19
20                for dr, dc in directions:
21                    r, c = row + dr, col + dc
22                    if (r in range(rows) and
23                        c in range(cols) and
24                        grid[r][c] == "1" and
25                        (r, c) not in visit):
26                        q.append((r, c))
27                        visit.add((r, c))
28
29        for r in range(rows):
30            for c in range(cols):
31                if grid[r][c] == "1" and (r, c) not in visit:
32                    bfs(r, c)
33                    islands += 1
34        return islands