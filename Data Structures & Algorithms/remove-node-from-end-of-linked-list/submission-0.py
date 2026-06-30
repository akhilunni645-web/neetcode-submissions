# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # Create dummy node
        dummy = ListNode(0, head)

        first = head
        second = dummy

        # Move first pointer n steps ahead
        for _ in range(n):
            first = first.next

        # Move both pointers together
        while first:
            first = first.next
            second = second.next

        # Remove nth node from end
        second.next = second.next.next

        return dummy.next