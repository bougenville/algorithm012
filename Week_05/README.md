# 期中复习
## 第一周

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
- [11. 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/)
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res
```
- [283. 移动零](https://leetcode-cn.com/problems/move-zeroes/)
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(0,len(nums)) :
            if (nums[i] != 0) :
                nums[j] = nums[i];
                if (i != j) :
                    nums[i] = 0;
                j += 1
```
- [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if (n <= 2): return n
        f1, f2, f3 = 1, 2, 3
        for i in range(3, n+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3
```
- [15. 三数之和](https://leetcode-cn.com/problems/3sum/)
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        nums = sorted(counts)
        for i, num in enumerate(nums):
            if counts[num] > 1:
                if num == 0:
                    if counts[num] > 2:
                        ans.append([0, 0, 0])
                else:
                    if -num * 2 in counts:
                        ans.append([num, num, -2 * num])
            if num < 0:
                two_sum = -num
                left = bisect.bisect_left(nums, (two_sum - nums[-1]), i + 1)
                for i in nums[left: bisect.bisect_right(nums, (two_sum // 2), left)]:
                    j = two_sum - i
                    if j in counts and j != i:
                        ans.append([num, i, j])
        return ans
```
- [206. 反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
```
- [24. 两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)
```python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
```
- [141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)
```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
```
- [142. 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)
```python
class Solution(object):
    def detectCycle(self, head):
        fast = slow = head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
```
- [25. K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)
```python
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        for _ in range(k):
            if not cur: return head
            cur = cur.next
        pre = head
        itera = head.next
        for _ in range(k-1):
            next = itera.next
            itera.next = pre
            pre = itera
            itera = next
        head.next = self.reverseKGroup(cur, k)
        return pre
```
- [22. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            :return:
            """
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return res
```
- [155. 最小栈](https://leetcode-cn.com/problems/min-stack/)
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```
- [84. 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)
```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
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
- [641. 设计循环双端队列](https://leetcode-cn.com/problems/design-circular-deque/)
```python
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        import collections
        self.size = k
        self.deque = collections.deque()


    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.deque.appendleft(value)
            return True
        return False


    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.deque.append(value)
            return True
        return False


    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.deque.popleft()
            return True
        return False


    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.deque.pop()
            return True
        return False


    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.isEmpty():
            return self.deque[0]
        return -1


    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.isEmpty():
            return self.deque[-1]
        return -1


    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return len(self.deque) == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.deque) == self.size
```
- [42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/)
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        # 边界条件
        if not height: return 0
        n = len(height)

        left,right = 0, n - 1  # 分别位于输入数组的两端
        maxleft,maxright = height[0],height[n - 1]
        ans = 0

        while left <= right:
            maxleft = max(height[left],maxleft)
            maxright = max(height[right],maxright)
            if maxleft < maxright:
                ans += maxleft - height[left]
                left += 1
            else:
                ans += maxright - height[right]
                right -= 1
        return ans
```
- [26. 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
```
- [189. 旋转数组](https://leetcode-cn.com/problems/rotate-array/)
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        lenth = len(nums)
        nums[:] = nums[lenth - k:] + nums[:lenth - k]
```
- [21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)
```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
```
- [88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m and n:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        while n:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
```
- [66. 加一](https://leetcode-cn.com/problems/plus-one/)
```python
class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                num = digits[i]
                digits[i] = num + 1
                break
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits
```
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
