'''
leetcode: 547

班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果 M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

示例 1：
输入：
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出：2 
解释：已知学生 0 和学生 1 互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回 2 。

示例 2：
输入：
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出：1
解释：已知学生 0 和学生 1 互为朋友，学生 1 和学生 2 互为朋友，所以学生 0 和学生 2 也是朋友，所以他们三个在一个朋友圈，返回 1 。
 

提示：

1 <= N <= 200
M[i][i] == 1
M[i][j] == M[j][i]

来源：力扣（LeetCode）
链接：https://leetcode cn.com/problems/friend circles
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        class UnionFind(object):
            def __init__(self, size):
                self.p = [i for i in range(size + 1)]
                self.num = size

            def find(self, x:int):
                # 路径压缩的并查集
                if self.p[x] != x:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]
            
            def union(self, a:int, b:int):
                if self.find(a) != self.find(b):
                    self.p[self.find(a)] = self.p[self.find(b)]
                    self.num -= 1
        
        n = len(M)
        if n == 1: return 1
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j]:
                    uf.union(i, j)
        return uf.num
