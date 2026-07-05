# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

       

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while stack or curr:

            # Go to leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left

            # Visit node
            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val

            # Move to right subtree
            curr = curr.right        