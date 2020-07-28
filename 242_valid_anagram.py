'''
leetcode: 242

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

说明: 你可以假设字符串只包含小写字母。

进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-anagram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
1. clarification
2. possible solutions --> optimal (time & space)
3. code
4. test cases
'''

#class Solution:
#    def isAnagram(self, s: str, t: str) -> bool:
#        if len(s) != len(t): return False
#        se = set(s)
#        if se == set(t):
#            for i in se:
#                # 直接比较字符元素个数比较字符的个数
#                if s.count(i) != t.count(i):return False
#            return True
#        else:
#            return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if sorted(s) != sorted(t):
            return False
        return True
