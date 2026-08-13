# Last updated: 8/12/2026, 11:54:22 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        if root is None:
10            return
11
12        memo = []
13
14        def dfs(node):
15            if not node: return
16
17            memo.append(node.val)
18            dfs(node.left)
19            dfs(node.right)
20        
21        dfs(root)
22        memo = sorted(memo)
23        return memo[k-1]