'''
leetcode: 212

给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:

你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def findWords(self, board, words) :
        WORD_END = '#'
        self.memo={}

        for word in words:
            cur_node = self.memo
            for letter in word:  #下面三行等效于cur_node=setdefault(letter,{})
                if letter not in cur_node:
                    cur_node[letter] = {}  #新建一个
                cur_node = cur_node[letter]  #不管有没有，进一位
            cur_node[WORD_END] = word  #表示这个单词结束,记录单词日后好调用

        row_num, column_num, ans = len(board), len(board[0]), []

        def backtrack(row, col, parent):
            letter = board[row][col]
            cur_node = parent[letter]

            if WORD_END in cur_node:
                ans.append(cur_node[WORD_END])  #当时记录的是那个完整单词
                cur_node.pop(WORD_END)  #剪枝

            board[row][col] = '#'  #代表被占用了，防止后续转回来

            for (delta_x, delta_y) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_row, next_col = row + delta_x, col + delta_y
                if not (0 <= next_row < row_num and 0 <= next_col < column_num): continue
                elif board[next_row][next_col] not in cur_node: continue
                else: backtrack(next_row, next_col, cur_node)

            board[row][col]=letter  #还原回去

            if not cur_node:  #这个是剪枝，从后往前剪枝
                parent.pop(letter)

        for row in range(row_num):
            for col in range(column_num):
                if board[row][col] in self.memo:
                    backtrack(row, col, self.memo)

        return ans
