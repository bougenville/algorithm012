'''
leetcode: 126

给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：
a. 每次转换只能改变一个字母。
b. 转换后得到的单词必须是字典中的单词。

说明:
1. 如果不存在这样的转换序列，返回一个空列表。
2. 所有单词具有相同的长度。
3. 所有单词只由小写字母组成。
4. 字典中不存在重复的单词。
5. 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

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
