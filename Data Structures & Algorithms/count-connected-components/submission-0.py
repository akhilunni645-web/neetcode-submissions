class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
    


        parent = [i for i in range(n)]
        size = [1] * n

        res = n

        def find(node):

            while node != parent[node]:

                parent[node] = parent[parent[node]]
                node = parent[node]

            return node

        def union(n1, n2):

            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0

            if size[p1] > size[p2]:

                parent[p2] = p1
                size[p1] += size[p2]

            else:

                parent[p1] = p2
                size[p2] += size[p1]

            return 1

        for n1, n2 in edges:
            res -= union(n1, n2)

        return res