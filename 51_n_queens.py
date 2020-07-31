'''
leetcode: 51

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]

解释: 4 皇后问题存在两个不同的解法。

提示： 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。
当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。
（引用自 百度百科 - 皇后 ）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def valid(row, col, track):#track用来记录皇后放置的列号
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
