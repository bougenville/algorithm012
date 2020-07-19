'''
leetcode: 350
'''

from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        ans = []
        for n in nums2:
            if n in c1 and c1[n] > 0:
                ans.append(n)
                c1[n] -= 1
        return ans

