# Last updated: 8/6/2026, 10:29:35 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    val = list()
9    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
10        if root is None:
11            return False
12
13        memo = []
14        res = list()
15        
16        def dfs(node):
17            if node is None:
18                return
19
20            memo.append(node.val)
21            if node.left is None and node.right is None:
22                res.append(sum(memo))
23            dfs(node.left)
24            dfs(node.right)
25            memo.pop()
26
27        dfs(root)
28        if targetSum in res:
29            return True
30        else:
31            return False