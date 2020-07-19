'''
leetcode: 66
'''

class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                num = digits[i]
                digits[i] = num + 1
                break
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits
