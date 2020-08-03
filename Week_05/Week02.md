## 第二周

- [242. 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/)
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        se = set(s)
        if se == set(t):
            for i in se:
                # 直接比较字符元素个数比较字符的个数
                if s.count(i) != t.count(i):return False
            return True
        else:
            return False
```
- [49. 字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())
```
- [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for x,num in enumerate(nums):
            h[num] = x
        for i,num in enumerate(nums):
            j = h.get(target - num)
            if j and i != j:
                return [i,j]
```
- [94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)
```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root):
            return helper(root.left) + [root.val] + helper(root.right) if root else []
        return helper(root)
```
- [144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)
```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root: return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
```
- [590. N叉树的后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)
```python
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def postHelper(root):
            if not root:
                return None
            children = root.children
            for child in children:
                postHelper(child)
            res.append(root.val)

        postHelper(root)
        return res
```
- [589. N叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/)
```python
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        s,res = [root],[]
        while s:
            node = s.pop()
            res.append(node.val)
            s.extend(node.children[::-1])
        return res
```
- [429. N叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/)
```python
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        queue = [root]
        res = []
        while queue:
            res.append(node.val for node in queue)
            queue = [child for node in queue for child in node.children]
        return res
```
- [239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        window, res = [], []
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res
```
- [264. 丑数](https://leetcode-cn.com/problems/ugly-number-ii/)
```python
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
```
- [347. 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/)
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        queue, res = [], []
        for i in dic:
            heapq.heappush(queue, (-dic[i], i))
        for i in range(k):
            tmp = heapq.heappop(queue)
            res.append(tmp[1])
        return res
```
