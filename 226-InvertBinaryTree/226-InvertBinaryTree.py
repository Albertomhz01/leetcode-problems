# Last updated: 8/2/2026, 9:20:48 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
10        if not root:
11            return
12
13        # print(f"root: {root.val}")
14        # root.left, root.right = root.right, root.left
15        
16        def DFS(node):
17            if not node:
18                return
19            node.left, node.right = node.right, node.left
20            DFS(node.left)
21            DFS(node.right)
22        
23        DFS(root)
24        return root