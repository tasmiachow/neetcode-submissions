"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key = lambda x: x.start)
        for i in range(1, len(intervals)):
            prev = sorted_intervals[i-1]
            curr = sorted_intervals[i]

            if prev.start > curr.start or prev.end > curr.start or prev.end > curr.end: 
                return False
        return True
         