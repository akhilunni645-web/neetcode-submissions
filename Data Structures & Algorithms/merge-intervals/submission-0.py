class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        from typing import List

        # Step 1: Sort intervals by start time
        intervals.sort()

        # Step 2: Add the first interval to the result
        result = [intervals[0]]

        # Step 3: Traverse the remaining intervals
        for start, end in intervals[1:]:

            # Last interval in the result
            lastEnd = result[-1][1]

            # If overlapping, merge intervals
            if start <= lastEnd:
                result[-1][1] = max(lastEnd, end)

            # Otherwise, add the current interval
            else:
                result.append([start, end])

        return result