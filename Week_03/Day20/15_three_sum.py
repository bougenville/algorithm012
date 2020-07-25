'''
leetcode: 15

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例： 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        res, i = [], 0
        for i in range(len(nums) - 2):
            if nums[i] > 0: break # 1. because of r > l > i.
            if i > 0 and nums[i] == nums[i - 1]: continue # 2. skip the same `nums[i]`.
            l, r = i + 1, len(nums) - 1
            while l < r: # 3. double pointer
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                    #while l < r and nums[l] == nums[l - 1]: l += 1
                elif s > 0:
                    r -= 1
                    #while l < r and nums[r] == nums[r + 1]: r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
        return res
