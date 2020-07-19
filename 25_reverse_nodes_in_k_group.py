'''
leetcode: 25
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        for _ in range(k):
            if not cur: return head
            cur = cur.next
        pre = head
        itera = head.next
        for _ in range(k-1):
            next = itera.next
            itera.next = pre
            pre = itera
            itera = next
        head.next = self.reverseKGroup(cur, k)
        return pre
