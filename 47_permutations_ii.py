'''
leetcode: 47

给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例: 输入: [1,1,2]

输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
	nums.sort()
	n = len(nums)
	visited = [0] * n
	res = []

	def helper1(temp_list, length):
            if length == n: res.append(temp_list)
            for i in range(n):
	        if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                    continue
                visited[i] = 1
	        helper1(temp_list + [nums[i]], length + 1)
	        visited[i] = 0

	def helper2(nums, temp_list, length):
            if length == n and temp_list not in res: res.append(temp_list)
		for i in range(len(nums)):
	            helper2(nums[:i] + nums[i+1:], temp_list + [nums[i]], length + 1)

	helper1([], 0)
	return res
