"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort by start time
        interval_list = []

        for i in range(len(intervals)):
            interval_list.append((intervals[i].start, intervals[i].end))
        
        sorted_list = sorted(interval_list)

        # Check conflict
        for i in range(len(sorted_list) - 1):
            if sorted_list[i][1] > sorted_list[i+1][0]:
                return False
        
        return True