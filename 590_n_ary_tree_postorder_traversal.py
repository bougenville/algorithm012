'''
leetcode: 590
'''

# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def postHelper(root):
            if not root:
                return None
            children = root.children
            for child in children:
                postHelper(child)
            res.append(root.val)

        postHelper(root)
        return res
