'''
leetcode: 1021
'''

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        res = ''
        for i in S:
            if i == '(':
                stack.append(i)
                if len(stack) > 1:
                    res += '('
            else:
                stack.pop()
                if len(stack) != 0:
                    res += ')'
        return res
