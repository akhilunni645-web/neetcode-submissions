class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        import heapq

class Solution:
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            dist = x * x + y * y

            heapq.heappush(heap, (-dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while heap:
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result