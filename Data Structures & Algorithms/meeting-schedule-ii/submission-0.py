"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0

        start = []
        end = []

        # Store all start and end times
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        # Sort both arrays
        start.sort()
        end.sort()

        s = 0
        e = 0

        count = 0
        res = 0

        while s < len(intervals):

            # Need a new room
            if start[s] < end[e]:
                count += 1
                res = max(res, count)
                s += 1

            # A room becomes free
            else:
                count -= 1
                e += 1

        return res