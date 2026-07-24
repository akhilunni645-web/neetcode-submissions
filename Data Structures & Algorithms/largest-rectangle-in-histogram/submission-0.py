class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        stack = []              # (start_index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i

            # Pop while current height is smaller or equal
            while stack and stack[-1][1] >= h:
                index, height = stack.pop()

                area = height * (i - index)
                maxArea = max(maxArea, area)

                # Current bar can extend back to the popped bar's start
                start = index

            stack.append((start, h))

        # Process remaining bars
        n = len(heights)

        for index, height in stack:
            area = height * (n - index)
            maxArea = max(maxArea, area)

        return maxArea