class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        



        heap = []

        # Build first window
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        res = [-heap[0][0]]

        l = 1

        for r in range(k, len(nums)):

            heapq.heappush(heap, (-nums[r], r))

            # Remove elements outside window
            while heap[0][1] < l:
                heapq.heappop(heap)

            res.append(-heap[0][0])

            l += 1

        return res        