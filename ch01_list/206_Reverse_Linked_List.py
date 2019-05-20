# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #def reverseList(self, head: ListNode) -> ListNode:
    #    prev, curr = None, head 
    #    while curr is not None:
    #        next_temp = curr.next
    #        curr.next = prev
    #        prev = curr
    #        curr = next_temp 
    #    return prev



    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
        

