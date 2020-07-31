'''
leetcode: 264

编写一个程序，找出第 n 个丑数。
丑数就是质因数只包含 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

说明:  
1. 1 是丑数。
2. n 不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def nthUglyNumber(self, n):
        dp = [1 for _ in range(n)]
        i2, i3, i5 = 0, 0, 0
        for i in range(1, n):
            min_val = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
            dp[i] = min_val
            if dp[i2] * 2 == min_val:
                i2 += 1
            if dp[i3] * 3 == min_val:
                i3 += 1
            if dp[i5] * 5 == min_val:
                i5 += 1
        return dp[-1]
