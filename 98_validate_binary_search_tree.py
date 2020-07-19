'''
leetcode: 98
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.pre = -float('inf')
        def inorder(node):
            if not node:
                return True
            if not inorder(node.left) or self.pre>=node.val:
                return False
            self.pre = node.val
            return inorder(node.right)
        return inorder(root)
