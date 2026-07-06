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
    def maxPathSum(self, root):
        self.maxSum = float("-inf")

        def dfs(node):
            if not node:
                return 0

            # Get max contribution from left and right
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Path passing through current node
            currentPath = node.val + left + right

            # Update global answer
            self.maxSum = max(self.maxSum, currentPath)

            # Return one side to parent
            return node.val + max(left, right)

        dfs(root)
        return self.maxSum