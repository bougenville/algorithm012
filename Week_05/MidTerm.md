## 第一周

- [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for x, num in enumerate(nums):
            h[num] = x
        for i, num in enumerate(nums):
            j = h.get(target - num)
            if j and i != j:
                return [i, j]
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
		if not nums: return 0
		# 两个指针 i 和 j
		j = 0
		for i in range(len(nums)):
			# 当前元素 != 0，就把其交换到左边，等于 0 的交换到右边
			if nums[i]:
				nums[j], nums[i] = nums[i], nums[j]
				j += 1
```
- [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
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
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        res, i = [], 0
        for i in range(len(nums) - 2):
            if nums[i] > 0: break                               # 1. because of r > l > i.
            if i > 0 and nums[i] == nums[i - 1]: continue       # 2. skip the same `nums[i]`.
            l, r = i + 1, len(nums) - 1
            while l < r:                                        # 3. double pointer
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
        return res
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
        for _ in range(k - 1):
            next = itera.next
            itera.next = pre
            pre = itera
            itera = next
        head.next = self.reverseKGroup(cur, k)
        return pre
```
- [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_map = {')':'(',']':'[','}':'{'}
        for c in s:
            if c not in paren_map:
                stack.append(c)
            elif not stack or paren_map[c] != stack.pop():
                return False
        return not stack
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
## 第三周

- [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        f1, f2, f3 = 1, 2, 3
        for i in range(3, n + 1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3
```
- [22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)
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
- [226. 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/)
```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        else:
            root.left, root.right = root.right, root.left
            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)
        return root
```
- [98. 验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)
```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.pre = -float('inf')
        def inorder(node):
            if not node:
                return True
            if not inorder(node.left) or self.pre>=node.val:
                return False
            self.pre = node.val
            return inorder(node.right)
        return inorder(root)
```
- [104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)
```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```
- [111. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)
```python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return left + right  + 1 if (left == 0 or right == 0) else min(left, right) + 1
```
- [297. 二叉树的序列化与反序列化](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/)
```python
class Codec:

    def serialize(self, root):
        """
        Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: res.append("null")
        return '[' + ','.join(res) + ']'


    def deserialize(self, data):
        """
        Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data=='[]':
            return None
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root
```
- [236. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return
        if not left: return right
        if not right: return left
        return root
```
- [105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:  # 递归终止条件
            return
        root = TreeNode(preorder[0])  # 先序为“根左右”，所以根据preorder可以确定root
        idx = inorder.index(preorder[0])  # 中序为“左根右”，根据root可以划分出左右子树
        # 下面递归对root的左右子树求解即可
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root
```
- [77. 组合](https://leetcode-cn.com/problems/combinations/)
```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or k > n: return []
        res = []
        self.__dfs(1, k, n, [], res)
        return res

    def __dfs(self, start, k, n, pre, res):
        if len(pre) == k:
            res.append(pre[:])
            return

        # 注意：这里 i 的上限是归纳得到的
        for i in range(start, n - (k - len(pre)) + 2):
            pre.append(i)
            self.__dfs(i + 1, k, n, pre, res)
            pre.pop()
```
- [46. 全排列](https://leetcode-cn.com/problems/permutations/)
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res
```
- [47. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/)
```python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
	nums.sort()
	n = len(nums)
	visited = [0] * n
	res = []

	def helper1(temp_list, length):
            if length == n: res.append(temp_list)
            for i in range(n):
	        if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                    continue
                visited[i] = 1
	        helper1(temp_list + [nums[i]], length + 1)
	        visited[i] = 0

	def helper2(nums, temp_list, length):
            if length == n and temp_list not in res: res.append(temp_list)
		for i in range(len(nums)):
	            helper2(nums[:i] + nums[i + 1:], temp_list + [nums[i]], length + 1)

	helper1([], 0)
	return res
```
- [50. Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0: return 0.0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res
```
- [78. 子集](https://leetcode-cn.com/problems/subsets/)
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, n= [], len(nums)
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])
        helper(0, [])
        return res
```
- [169. 多数元素](https://leetcode-cn.com/problems/majority-element/)
```python
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
```
- [17. 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)
```python
class Solution(object):
    def letterCombinations(self, digits):
        '''
        :type digits: str
        :rtype List[str]
        '''
        if not digits: return []
        d = [' ', '*', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []

        def dfs(tmp, index):
            if index == len(digits):
                res.append(tmp)
                return
            c = digits[index]
            letters = d[ord(c) - 48]
            for i in letters:
                dfs(tmp + i, index + 1)

        dfs('', 0)
        return res
```
- [51. N皇后](https://leetcode-cn.com/problems/n-queens/)
```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def valid(row, col, track):  # track 用来记录皇后放置的列号
            if col in track:  # 判列 如果这一列已经放置过皇后
                return False
            for k in range(row):  # 判斜对角
                if row + col == k + track[k] or row - col == k - track[k]:
                    return False
            return True

        def backtrack(row, tmp):
            if row == n:  # 已到最后一行
                res.append(tmp)
                return
            for col in range(n):
                # 若位置合法，则进入下一行
                if valid(row, col, tmp):
                    backtrack(row + 1, tmp + [col])

        res = []
        backtrack(0, [])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in j] for j in res]
```
## 第四周

- [102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)
```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], []
        queue.append(root)
        while queue:
            curr_level_size = len(queue)
            res.append([])
            index = 1
            while index <= curr_level_size:
                node = queue.pop(0)
                res[-1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                index += 1
        return res
```
- [433. 最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/)
```python
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        genes = ["A", "C", "G", "T"]
        queue = [(start, 0)]
        while queue:
            (res, step) = queue.pop(0)
            if res == end:
                return step
            for i in range(len(res)):
                for g in genes:
                    tmp = res[:i] + g + res[i + 1:]
                    if tmp in bank:
                        bank.remove(tmp)
                        queue.append((tmp, step + 1))
        return -1
```
- [22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)
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
- [515. 在每个树行中找最大值](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/)
```python
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root, depth):
            if not root: return
            if len(res) <= depth:
                res.append(float("-inf"))
            res[depth] = max(res[depth], root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        return res
```
- [127. 单词接龙](https://leetcode-cn.com/problems/word-ladder/)
```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wordict = set(wordList)
        s1, s2, n = {beginWord}, {endWord}, len(beginWord)
        step = 0
        wordict.remove(endWord)
        while s1 and s2:
            step += 1
            if len(s1) > len(s2): s1, s2 = s2, s1
            s = set()
            for word in s1:
                nextword = [word[:i] + chr(j) + word[i + 1:] for j in range(97, 123) for i in range(n)]
                for w in nextword:
                    if w in s2:
                        return step + 1
                    if w not in wordict: continue
                    wordict.remove(w)
                    s.add(w)
            s1 = s
        return 0
```
- [126. 单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii/)
```python
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        #键是点，值是到达该点所经过的轨迹
        layer = {}
        layer[beginWord] = [[beginWord]]
        while layer:
            newlayer = defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            newword = w[:i] + c + w[i + 1:]
                            if newword in wordList:
                                newlayer[newword] += [j + [newword] for j in layer[w]]
            #删除已经访问过的点
            wordList -= newlayer.keys()
            layer = newlayer
        return res
```
- [200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1

        return count

    def dfs(self, grid, i, j):
        if (i < 0 or j < 0 or i >= len(grid)
                or j >= len(grid[0])
                or grid[i][j] != '1'):
            return
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
```
- [529. 扫雷游戏](https://leetcode-cn.com/problems/minesweeper/)
```python
d = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        a, b = click
        if board[a][b] == 'M':
            board[a][b] = 'X'
        elif board[a][b] == 'E':
            m, n = len(board), len(board[0])
            def f(i, j):
                c = 0
                for di, dj in d:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n:
                        c += board[x][y] == 'M'
                if c:
                    board[i][j] = str(c)
                else:
                    board[i][j] = 'B'
                    for di, dj in d:
                        x, y = i + di, j + dj
                        0 <= x < m and 0 <= y < n and board[x][y] == 'E' and f(x, y)
            f(a, b)
        return board
```
- [860. 柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/)
```python
class Solution(object):
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
```
- [122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0: profit += tmp
        return profit
```
- [455. 分发饼干](https://leetcode-cn.com/problems/assign-cookies/)
```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child  = 0
        cookie = 0
        while  child <len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child
```
- [874. 模拟行走机器人](https://leetcode-cn.com/problems/walking-robot-simulation/)
```python
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 字典存储某个方向(key)对应的 [x方向移动，y方向移动，当前方向的左侧，当前方向的右侧] (val)
        direction = {'up': [0, 1, 'left', 'right'],
                     'down': [0, -1, 'right', 'left'],
                     'left': [-1, 0, 'down', 'up'],
                     'right': [1, 0, 'up', 'down']}
        x, y = 0, 0
        dir = 'up'
        res = 0
        obstacles = set(map(tuple, obstacles))
        for command in commands:
            if command > 0:  # 正数的话进行模型行进操作
                for step in range(command):
                    if (x + direction[dir][0], y + direction[dir][1]) not in obstacles:
                        x += direction[dir][0]
                        y += direction[dir][1]
                        res = max(res, x ** 2 + y ** 2)
                    else:
                        break
            else:  # 负数的话只改变行进方向
                if command == -1:  # 右转
                    dir = direction[dir][3]
                else:  # 即command == -2，左转
                    dir = direction[dir][2]
        return res
```
- [55. 跳跃游戏](https://leetcode-cn.com/problems/jump-game/)
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False
```
