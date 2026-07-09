"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""



     # Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):

        if not node:
            return None

        oldToNew = {}

        def dfs(node):

            # Already cloned
            if node in oldToNew:
                return oldToNew[node]

            # Create copy
            copy = Node(node.val)

            # Save in hashmap
            oldToNew[node] = copy

            # Clone neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)   