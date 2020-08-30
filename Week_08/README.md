学习笔记

## 第八周

### 位运算
*N 皇后的位运算解法 - Python*

```python
def totalNQueens(self, and):
    if and < 1: return []
    self.count = 0
    self.DFS(n, 0, 0, 0, 0)
    return self.count

def DFS(self, n, row, cols, pie, na):
    # recursion terminator
    if row >= n:
       self.count += 1
       return

    bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 得到当前所有的空位

    while bits:
        p = bits & -bits  # 取到最低位的 1
        bits = bits & (bits - 1)  # 表示在 p 位置上放入皇后
        self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
        # 不需要 revert cols, pie, na 的状态
```
### 布隆过滤器、 LRU 缓存

*布隆过滤器*

```python
from bitarray import bitarray
import mmh3

class BloomFilter:
  def __init__(self, size, hash_num):
    self.size = size
    self.hash_num = hash_num
    self.bit_array = bitarray(size)
    self.bit_array.setall(0)
    
  def add(self, s):
    for seed in range(self.hash_num):
      result = mmh3.hash(s, seed) % self.size
      self.bit_array[result] = 1

  def lookup(self, s):
    for seed in range(self.hash_num):
      result = mmh3.hash(s, seed) % self.size
      if self.bit_array[result] == 0:
        return "Nope"
    return "Probably"

bf = BloomFilter(500000, 7)
bf.add("dantezhao")

print (bf.lookup("dantezhao"))
print (bf.lookup("yyj"))
```

*LRU Cache*

```python
class LRUCache(object):
  def __init__(self, capacity):
    self.dic = collections.OrderedDict()
    self.remain = capacity

  def get(self, key):
    if key not in self.dic:
      return -1
    v = self.dic.pop(key)
    self.dic[key] = v # key as the newest one
    return v

  def put(self, key, value):
    if key in self.dic:
      self.dic.pop(key)
    else:
      if self.remain > 0:
        self.remain -= 1
      else: # self.dic is full 
        self.dic.popitem(last=False)
    self.dic[key] = value
```
### 排序算法

1. 比较类排序
   - 交换排序
     - 冒泡排序
     - 快速排序
   - 插入排序
     - 简单插入排序
     - 希尔排序
   - 选择排序
     - 简单选择排序
     - 堆排序
   - 归并排序
     - 二路归并排序
     - 多路归并排序
2. 非比较类排序
   - 计数排序
   - 桶排序
   - 基数排序

#### 初级排序 （O(n^2)）
1. 选择排序（Selection Sort）
2. 插入排序（Insertion Sort）
3. 冒泡排序（Bubble Sort）

#### 高级排序 （O(N*LogN)）
1. 快速排序（Quick Sort）
2. 归并排序（Merge Sort） - 分治
3. 堆排序（Heap Sort）

#### 特殊排序 （O(n)）