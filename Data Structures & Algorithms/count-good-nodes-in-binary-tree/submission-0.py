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
    def goodNodes(self, root: TreeNode) -> int:

        self.count = 0

        def dfs(node, maxValue):
            if not node:
                return

            if node.val >= maxValue:
                self.count += 1

            maxValue = max(maxValue, node.val)

            dfs(node.left, maxValue)
            dfs(node.right, maxValue)

        dfs(root, root.val)

        return self.count