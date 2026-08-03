# Last updated: 8/3/2026, 5:05:57 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        if root is None:
10            return 0
11
12        left_depth = self.maxDepth(root.left)
13        right_depth = self.maxDepth(root.right)
14
15        return max(left_depth, right_depth) + 1