'''
leetcode: 264
'''

class Solution:
    def nthUglyNumber(self, n):
        from heapq import heappop, heappush
        seen = {1}
        nums = []
        heap = []
        heappush(heap, 1)

        while len(nums) < n:
            cur = heappop(heap)
            nums.append(cur)
            for i in [2, 3, 5]:
                num = cur * i
                if num not in seen:
                    seen.add(num)
                    heappush(heap, num)
        return nums[n-1]
