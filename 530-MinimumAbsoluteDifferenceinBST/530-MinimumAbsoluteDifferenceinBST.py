# Last updated: 7/31/2026, 2:48:16 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
9        prev, res = None, float("inf")
10
11        def dfs(node):
12            if not node:
13                return
14            dfs(node.left)
15            nonlocal prev, res
16            if prev:
17                res = min(res, node.val - prev.val)
18            prev = node
19            dfs(node.right)
20        
21        dfs(root)
22        return res