'''
leetcode: 94
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root):
            return helper(root.left) + [root.val] + helper(root.right) if root else []
        return helper(root)
