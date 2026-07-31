# Last updated: 7/31/2026, 2:37:02 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
9        vals = []
10        mini_val = float('inf')
11
12        def dfs(node):
13            if not node:
14                return
15            vals.append(node.val)
16            dfs(node.left)
17            dfs(node.right)
18
19        dfs(root)
20
21        for ii in range(len(vals)):
22            for kk in range(ii+1, len(vals)):
23                if abs(vals[ii] - vals[kk]) < mini_val:
24                    mini_val = abs(vals[ii]-vals[kk])
25        return mini_val