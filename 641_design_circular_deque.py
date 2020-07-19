'''
leetcode: 641
'''

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



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
