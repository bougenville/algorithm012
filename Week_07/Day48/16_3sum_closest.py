'''
leetcode: 16

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float('inf')
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            j, k = i + 1, len(nums) - 1
            if nums[i] + nums[i+1] + nums[i+2] > target:
                result = nums[i] + nums[i+1] + nums[i+2] if abs(nums[i] + nums[i+1] + nums[i+2] - target) < abs(result - target) else result
                break
            if nums[i] + nums[-1] + nums[-2] < target:
                result = nums[i] + nums[-1] + nums[-2] if abs(nums[i] + nums[-1] + nums[-2] - target) < abs(result - target) else result
                continue
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum == target:
                    return target
                elif cur_sum > target:
                    k -= 1
                else:
                    j += 1
                result = cur_sum if abs(cur_sum - target) < abs(result - target) else result
        return result
