# Last updated: 8/3/2026, 5:01:49 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
9        def DFS(left_root, right_root):
10            if not left_root and not right_root:
11                return True
12            if not left_root or not right_root:
13                return False
14            if left_root.val == right_root.val:
15                return DFS(left_root.left, right_root.right) and DFS(left_root.right, right_root.left)
16            else:
17                return False
18            
19        return DFS(root.left, root.right)
20        