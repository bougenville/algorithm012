'''
leetcode: 46

给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

#class Solution:
#    def permute(self, nums: List[int]) -> List[List[int]]:
#        res = []
#        def backtrack(nums, tmp):
#            if not nums:
#                res.append(tmp)
#                return
#            for i in range(len(nums)):
#                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
#        backtrack(nums, [])
#        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res
