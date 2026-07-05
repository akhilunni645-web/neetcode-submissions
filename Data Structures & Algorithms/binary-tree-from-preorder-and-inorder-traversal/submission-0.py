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
    def buildTree(self, preorder, inorder):
        inorderMap = {}

        for i, val in enumerate(inorder):
            inorderMap[val] = i

        self.preIdx = 0

        def dfs(left, right):
            if left > right:
                return None

            rootVal = preorder[self.preIdx]
            self.preIdx += 1

            root = TreeNode(rootVal)

            mid = inorderMap[rootVal]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)