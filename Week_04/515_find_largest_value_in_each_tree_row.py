'''
leetcode: 515

您需要在二叉树的每一行中找到最大的值。

示例：

输入:
          1
         / \
        3   2
       / \   \
      5   3   9

输出: [1, 3, 9]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root, depth):
            if not root: return
            if len(res) <= depth:
                res.append(float("-inf"))
            res[depth] = max(res[depth], root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        return res
