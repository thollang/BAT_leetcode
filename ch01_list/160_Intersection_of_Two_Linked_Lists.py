# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA, curB = headA, headB
        lenA, lenB = 0, 0
        while curA:
            lenA += 1
            curA = curA.next
        while curB:
            lenB += 1
            curB = curB.next
        curA, curB = headA, headB

        for i in range(abs(lenA-lenB)):
            if lenA > lenB:
                curA = curA.next
            elif lenB > lenA:
                curB = curB.next

        while curA != curB:
            curA, curB = curA.next, curB.next

        return curA