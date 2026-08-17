# Last updated: 8/17/2026, 12:10:57 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        def dfs(node, left, right):
10            if not node:
11                return True
12
13            if node.val <= left or node.val >= right:
14                return False
15
16            return (dfs(node.left, left, node.val) and
17                    dfs(node.right, node.val, right))
18
19        return dfs(root, float("-inf"), float("inf"))