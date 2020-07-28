学习笔记
## 第四周
## 第九课
### 深度优先搜索和广度优先搜索
#### DFS 代码模板

- 递归写法

```python

visited = set()

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited
    	return

	visited.add(node)

	# process current node here.
	...
	for next_node in node.children():
		if next_node not in visited:
			dfs(next_node, visited)
```

- 非递归写法

```python
def DFS(self, tree):

	if tree.root is None:
		return []

	visited, stack = [], [tree.root]

	while stack:
		node = stack.pop()
		visited.add(node)

		process (node)
		nodes = generate_related_nodes(node)
		stack.push(nodes)

	# other processing work
	...
```

#### BFS 代码模板

```python

def BFS(graph, start, end):
    visited = set()
	queue = []
	queue.append([start])

	while queue:
		node = queue.pop()
		visited.add(node)

		process(node)
		nodes = generate_related_nodes(node)
		queue.push(nodes)

	# other processing work
	...
```

## 第十课
### 贪心算法 (Greedy)

贪心算法是一种在每一步选择中都采取在当前状态下最好或最优(即最有利)的选择，从而希望导致结果是全局最好或最优的算法。

贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

适用贪心算法的场景: 简单地说，问题能够分解成子问题来解决，子问题的最优解能递推到最终问题的最优解。这种子问题最优解称为最优子结构。


### 实战题目
| 题号 | 名称 | 难度 | 分类 | 备注 |
| --- | --- | --- | --- | --- |
| [102](https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/?currentPage=1&orderBy=most_votes&query=) | [二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)| 🟡 中等 | 深度优先、广度优先 | - |
| [433](https://leetcode.com/problems/minimum-genetic-mutation/discuss/?currentPage=1&orderBy=most_votes&query=) | [最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/)| 🟡 中等 | 深度优先、广度优先 | - |
| [22](https://leetcode.com/problems/generate-parentheses/discuss/?currentPage=1&orderBy=most_votes&query=) | [括号生成](https://leetcode-cn.com/problems/generate-parentheses/)| 🟡 中等 | 深度优先、广度优先 | - |
| [515](https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/?currentPage=1&orderBy=most_votes&query=) | [在每个树行中找最大值](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/)| 🟡 中等 | 深度优先、广度优先 | - |
| [322](https://leetcode.com/problems/coin-change/discuss/?currentPage=1&orderBy=most_votes&query=) | [零钱兑换](https://leetcode-cn.com/problems/coin-change/)| 🟡 中等 | 动态规划 | - |
| [69](https://leetcode.com/problems/sqrtx/discuss/?currentPage=1&orderBy=most_votes&query=) | [x 的平方根](https://leetcode-cn.com/problems/sqrtx/)| 🟢 简单 | 二分查找 | - |
| [367](https://leetcode.com/problems/valid-perfect-square/discuss/?currentPage=1&orderBy=most_votes&query=) | [有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square/)| 🟢 简单 | 二分查找 | - |

### 课后作业

| 题号 | 名称 | 难度 | 分类 | 备注 |
| --- | --- | --- | --- | --- |
| [860](https://leetcode.com/problems/lemonade-change/discuss/?currentPage=1&orderBy=most_votes&query=) | [柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/)| 🟢 简单 | 贪心算法 | - |
| [122](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/?currentPage=1&orderBy=most_votes&query=) | [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)| 🟢 简单 | 贪心算法 | - |
| [455](https://leetcode.com/problems/assign-cookies/discuss/?currentPage=1&orderBy=most_votes&query=) | [分发饼干](https://leetcode-cn.com/problems/assign-cookies/)| 🟢 简单 | 贪心算法 | - |
| [874](https://leetcode.com/problems/walking-robot-simulation/discuss/?currentPage=1&orderBy=most_votes&query=) | [模拟行走机器人](https://leetcode-cn.com/problems/walking-robot-simulation/)| 🟢 简单 | 贪心算法 | - |
| [127](https://leetcode.com/problems/word-ladder/discuss/?currentPage=1&orderBy=most_votes&query=) | [单词接龙](https://leetcode-cn.com/problems/word-ladder/)| 🟡 中等 | 深度优先、广度优先 | - |
| [200](https://leetcode.com/problems/number-of-islands/discuss/?currentPage=1&orderBy=most_votes&query=) | [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)| 🟡 中等 | 深度优先、广度优先 | - |
| [529](https://leetcode.com/problems/minesweeper/discuss/?currentPage=1&orderBy=most_votes&query=) | [扫雷游戏](https://leetcode-cn.com/problems/minesweeper/)| 🟡 中等 | 深度优先、广度优先 | - |
| [55](https://leetcode.com/problems/jump-game/discuss/?currentPage=1&orderBy=most_votes&query=) | [跳跃游戏](https://leetcode-cn.com/problems/jump-game/)| 🟡 中等 | 贪心算法 | - |
| [33](https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/?currentPage=1&orderBy=most_votes&query=) | [搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)| 🟡 中等 | 二分查找 | - |
| [74](https://leetcode.com/problems/search-a-2d-matrix/discuss/?currentPage=1&orderBy=most_votes&query=) | [搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)| 🟡 中等 | 二分查找 | - |
| [153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/?currentPage=1&orderBy=most_votes&query=) | [寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)| 🟡 中等 | 二分查找 | - |
| [126](https://leetcode.com/problems/word-ladder-ii/discuss/?currentPage=1&orderBy=most_votes&query=) | [单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii/)| 🔴 困难 | 深度优先、广度优先 | - |
