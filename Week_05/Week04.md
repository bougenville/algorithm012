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
