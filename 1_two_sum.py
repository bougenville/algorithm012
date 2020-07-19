'''
leetcode: 1
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for x,num in enumerate(nums):
            h[num] = x
        for i,num in enumerate(nums):
            j = h.get(target - num)
            if j and i != j:
                return [i,j]
