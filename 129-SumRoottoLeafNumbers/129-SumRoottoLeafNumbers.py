# Last updated: 8/13/2026, 12:40:28 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumNumbers(self, root: Optional[TreeNode]) -> int:
9        if root is None:
10            return
11
12        memo = list()
13        res = list()
14
15        def dfs(node):
16            if node is None:
17                return
18            
19            nonlocal memo
20            memo.append(node.val)
21            if node.left is None and node.right is None:
22                res.append("".join(map(str, memo)))
23            dfs(node.left)
24            dfs(node.right)
25            memo.pop()
26
27        dfs(root)
28        for ii in range(len(res)):
29            res[ii] = int(res[ii])
30
31        return sum(res)