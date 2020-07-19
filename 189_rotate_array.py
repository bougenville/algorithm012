'''
leetcode: 189
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        lenth = len(nums)
        nums[:] = nums[lenth - k:] + nums[:lenth - k]
