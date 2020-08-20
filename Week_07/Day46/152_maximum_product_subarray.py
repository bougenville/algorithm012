'''
leetcode: 152

给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return
        cur_pro, min_pos = 1, 1
        max_neg, res = float("-inf"), float("-inf")

        for num in nums:
            cur_pro *= num
            # 考虑三种情况
            # 大于0
            if cur_pro > 0:
                res = max(res, cur_pro // min_pos)
                min_pos = min(min_pos, cur_pro)
            # 小于0
            elif cur_pro < 0:
                if max_neg != float("-inf"):
                    res = max(res, cur_pro // max_neg)
                else:
                    res = max(res, num)
                max_neg = max(max_neg, cur_pro)
            # 等于0
            else:
                cur_pro = 1
                min_pos = 1
                max_neg = float("-inf")
                res = max(res, num)
        return res·
