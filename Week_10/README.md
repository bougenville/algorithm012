# 毕业总结
摘自 https://github.com/jiangnanage 


### 五毒神掌(每道题至少做5遍以上)：
1. 第一遍不要死磕，要看代码学习（一定要看国际版的高票回答）；
2. 有思路：自己开始写代码；不然马上看题解，默写背诵熟练；
3. 24h 后第二遍开始自己写（闭卷）；
4. 第三遍隔天或者一周后再做一遍（时间紧的话，就只需要看脑图）；
5. 第四/五遍隔一周或者面试前再复盘一下

### 切题四件套： 
1. 先了解清楚题意；
1. 尽可能多的想不同题解；
1. 分析最优的解题；
1. 再写再测试

- 自顶向下编程方式  
- 最大误区：做题只做一遍  
- 优化思想：空间换时间、升维  

### 数据结构

- **一维**      
  - **基础**：数组 array，链表 linked list
  - **高级**：栈 stack， 队列 queue，双端队列 deque，集合 set，映射 map (hash) TreeMap、HashMap
- **二维**  
  - **基础**：树 tree，图 graph
  - **高级**：二叉搜索树 binary search tree(red-black tree,AVL)，堆 heap，并查集 disjoint set，字典树 trie
- **特殊**  
  - 位运算 Bitwise，布隆过滤器 BloomFilter
  - LRU Cache
  
### 复杂度分析

数据结构 | Access | Search | Insertion | Deletion
---|---|---|---|---
Array | O(1) | O(n) | O(n) | O(n) 
Stack | O(n) | O(n) | O(1) | O(1) 
Queue | O(n) | O(n) | O(1) | O(1) 
Singly-Linked List | O(n) | O(n) | O(1) | O(1)
Doubly-Linked List | O(n) | O(n) | O(1) | O(1)
Skip List | O(logN) | O(logN) | O(logN) | O(logN)
Hash Table | N/A | O(1) | O(1) | O(1)
Binary Search Tree | O(logN) | O(logN) | O(logN) | O(logN)
Cartesian Tree | N/A | O(logN) | O(logN) | O(logN)
B-Tree | O(logN) | O(logN) | O(logN) | O(logN)
Read-Black Tree | O(logN) | O(logN) | O(logN) | O(logN)
Splay Tree | N/A | O(logN) | O(logN) | O(logN)
AVL Tree | O(logN) | O(logN) | O(logN) | O(logN)
KD Tree | O(logN) | O(logN) | O(logN) | O(logN)

### 排序算法复杂度

排序方法 | 时间复杂度(平均) | 时间复杂度(最坏) | 时间复杂度(最好) | 空间复杂度 | 稳定性 
---|---|---|---|---|---
插入排序 | O(n^2) | O(n^2) | O(n) | O(1) | 稳定  
希尔排序 | O(n^1.3) | O(n^2) | O(n) | O(1) | 不稳定
选择排序 | O(n^2) | O(n^2) | O(n^2) | O(1) | 不稳定
堆排序 | O(nlog2^n)  | O(nlog2^n) | O(nlog2^n) | O(1) | 不稳定
冒泡排序 | O(n^2) | O(n^2) | O(n) | O(1) | 稳定
快速排序 | O(nlog2^n)  | O(n^2) | O(nlog2^n)  | O(nlog2^n) | 不稳定
归并排序 | O(nlog2^n)  | O(nlog2^n) | O(nlog2^n) | O(n) | 稳定
计数排序 | O(n+k) | O(n+k) | O(n+k) | O(n+k) | 稳定
桶排序 | O(n+k) | O(n^2) | O(n) | O(n+k) | 稳定
基数排序 | O(n*k) | O(n*k) | O(n*k) | O(n+k) | 稳定

### 化繁为简的思想
1. 人肉递归低效、很累-> 画出递归的状态树
2. 找到最近最简方法，将其拆解成可重复解决的问题
3. 数学归纳思维

### 学习要点
- 基本功是区别业余和职业选手的根本。深厚功底来自于——过遍数
- 最大的误区：只做一遍
- 五毒神掌
- 刻意练习 - 练习缺陷弱点地方、不舒服、枯燥
- 反馈-看题解、看国际版的高票回答


---

以下是我认为写的非常好的本期优秀学员的总结，摘录在这里。

1. https://github.com/shenlu89/algorithm012/tree/master/Week_10
1. https://github.com/manchungkali/algorithm012/tree/master/Week_10
1. https://github.com/FishPancake/algorithm012/blob/master/Week_10/algorithm012-毕业总结.md
1. https://github.com/lixuan-creator/algorithm012/tree/master/Week_10%20毕业总结
1. https://github.com/woshiamiaojiang/algorithm012/tree/master/Week_10
1. https://github.com/HolaAmigoV5/algorithm012/blob/master/README.md
1. https://github.com/jiangnanage/algorithm012/tree/master/Week_10