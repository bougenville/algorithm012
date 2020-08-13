'''
leetcode: 589

给定一个 N 叉树，返回其节点值的前序遍历。

说明: 递归法很简单，你可以使用迭代法完成此题吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        s, res = [root], []
        while s:
            node = s.pop()
            res.append(node.val)
            s.extend(node.children[::-1])
        return res
