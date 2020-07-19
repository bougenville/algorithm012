'''
leetcode: 589
'''

# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        s,res = [root],[]
        while s:
            node = s.pop()
            res.append(node.val)
            s.extend(node.children[::-1])
        return res
