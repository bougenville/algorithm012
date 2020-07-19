'''
leetcode: 429
'''

# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        queue = [root]
        res = []
        while queue:
            res.append(node.val for node in queue)
            queue = [child for node in queue for child in node.children]
        return res
