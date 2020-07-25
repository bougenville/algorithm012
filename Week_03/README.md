# 课程表

## 第七课
### 泛型递归、树的递归

前序回顾：树的面试题解法一般都是 **递归**

1. 节点的定义
2. 重复（自相似）性

示例代码
```python
def preorder(self, root):
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

def inorder(self, root):
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)

def postorder(self, root):
    if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path.append(root.val)
```

#### 递归（Recursion）

递归 - 循环
>通过函数体来进行的循环

例如：计算 n!


n!= 1 * 2 * 3 * ... * n

```python
def Factorial(n):
    if n <= 1:
        return 1
    return n * Factorial(n — 1)
```

Python 代码模版
```python
def recursion(level, param1, param2, ...):
     # recursion terminator
     if level > MAX_LEVEL:
       process_result
       return
     # process logic in current level
     process(level, data...)
     # drill down
     self.recursion(level + 1, p1, ...)
     # reverse the current level status if needed
```
##  第八课
### 分治、回溯

#### 分治（Divide & Conquer）

分治代码模板

```python
def divide_conquer(problem, param1, param2, ...):
  # recursion terminator
  if problem is None:
    print_result
    return
  # prepare data
  data = prepare_data(problem)
  subproblems = split_problem(problem, data)
  # conquer subproblems
  subresult1 = self.divide_conquer(subproblems[0], p1, ...)
  subresult2 = self.divide_conquer(subproblems[1], p1, ...)
  subresult3 = self.divide_conquer(subproblems[2], p1, ...)
  ...
  # process and generate the final result
  result = process_result(subresult1, subresult2, subresult3, ...)
  # revert the current level states
```

#### 回溯（Backtracking）
回溯法采用试错的思想，它尝试分步地去解决一个问题。在分步解决问题的过程中，当它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案。

回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况:
 - 找到一个可能存在的正确的答案
 - 在尝试了所有可能的分步方法后宣告该问题没有答案

在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。

## 第三周
### 实战
| 题号 | 名称 | 难度 | 分类 | 备注 |
| --- | --- | --- | --- | --- |
| [70](https://leetcode.com/problems/climbing-stairs/discuss/?currentPage=1&orderBy=most_votes&query=) | [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)| 🟢 简单 | 泛型递归、树的递归 | - |
| [22](https://leetcode.com/problems/generate-parentheses/discuss/?currentPage=1&orderBy=most_votes&query=) | [括号生成](https://leetcode-cn.com/problems/generate-parentheses/)| 🟡 中等 | 泛型递归、树的递归 | - |
| [50](https://leetcode.com/problems/powx-n/discuss/?currentPage=1&orderBy=most_votes&query=) | [Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)| 🟡 中等 | 分治、回溯 | - |
| [78](https://leetcode.com/problems/subsets/discuss/?currentPage=1&orderBy=most_votes&query=) | [子集](https://leetcode-cn.com/problems/subsets/)| 🟡 中等 | 分治、回溯 | - |
| [17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/?currentPage=1&orderBy=most_votes&query=) | [电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)| 🟡 中等 | 分治、回溯 | - |
| [51](https://leetcode.com/problems/n-queens/discuss/?currentPage=1&orderBy=most_votes&query=) | [N皇后](https://leetcode-cn.com/problems/n-queens/)| 🔴 困难 | 分治、回溯 | - |


### 课后作业
| 题号 | 名称 | 难度 | 分类 | 备注 |
| --- | --- | --- | --- | --- |
| [236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/?currentPage=1&orderBy=most_votes&query=) | [二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)| 🟡 中等 | 泛型递归、树的递归 | - |
| [105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/?currentPage=1&orderBy=most_votes&query=) | [从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)| 🟡 中等 | 泛型递归、树的递归 | - |
| [77](https://leetcode.com/problems/combinations/discuss/?currentPage=1&orderBy=most_votes&query=) | [组合](https://leetcode-cn.com/problems/combinations/)| 🟡 中等 | 泛型递归、树的递归 | - |
| [46](https://leetcode.com/problems/permutations/discuss/?currentPage=1&orderBy=most_votes&query=) | [全排列](https://leetcode-cn.com/problems/permutations/)| 🟡 中等 | 泛型递归、树的递归 | - |
| [47](https://leetcode.com/problems/permutations-ii/discuss/?currentPage=1&orderBy=most_votes&query=) | [全排列 II](https://leetcode-cn.com/problems/permutations-ii/)| 🟡 中等 | 泛型递归、树的递归 | - |
