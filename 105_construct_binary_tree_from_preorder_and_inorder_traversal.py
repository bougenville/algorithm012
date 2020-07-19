'''
leetcode: 105
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:  # 递归终止条件
            return
        root = TreeNode(preorder[0])  # 先序为“根左右”，所以根据preorder可以确定root
        idx = inorder.index(preorder[0])  # 中序为“左根右”，根据root可以划分出左右子树
        # 下面递归对root的左右子树求解即可
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root
