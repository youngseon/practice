# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        Nth = None
        curr = head
        cumul = 0
        while(curr != None):
            if (cumul >= n):
                Nth = head if Nth==None else Nth.next
            cumul += 1
            curr = curr.next
        
        if (Nth == None):
            head = head.next
        else:
            Nth.next = (Nth.next).next
        return head