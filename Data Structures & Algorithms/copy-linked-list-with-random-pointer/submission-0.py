"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""



  # Definition for a Node.
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return None

        # old node -> new node
        copyMap = {}

        # First pass: create all copied nodes
        curr = head
        while curr:
            copyMap[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: assign next and random pointers
        curr = head
        while curr:
            copy = copyMap[curr]

            copy.next = copyMap.get(curr.next)
            copy.random = copyMap.get(curr.random)

            curr = curr.next

        # Return copied head
        return copyMap[head]      