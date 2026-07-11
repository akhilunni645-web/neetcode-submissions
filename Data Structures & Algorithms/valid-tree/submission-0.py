class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

    
        # Build adjacency list
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()

        def dfs(node, parent):

            # Cycle detected
            if node in visit:
                return False

            visit.add(node)

            for nei in graph[node]:

                # Don't go back to parent
                if nei == parent:
                    continue

                if not dfs(nei, node):
                    return False

            return True

        # Detect cycle
        if not dfs(0, -1):
            return False

        # Check graph is connected
        return len(visit) == n