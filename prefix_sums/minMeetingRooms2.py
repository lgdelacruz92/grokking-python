import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ans = 0
        n = len(intervals)
        if n == 0:
            return ans
        
        # the intervals must be sorted
        intervals.sort(key=lambda x:x[0])

        # the current item will either need a new room or not
        # intervals[i] represents the current slot
        # needs to find the next available room
        # the current item will take the next available room
        # min_heap can represent the next available room
        # [(intervals[0],intervals[0][1])]
        # min_heap will always have the next room that is going to finish
        # the soonest
        # If the soonest ending is less than the current_slot then I can pop
        # the soonest and push the current_slot in the heap

        min_heap = [] # [(weight, start, end)]represents the next available room
        ans = 0
        for i in range(n):
            while min_heap and min_heap[0][2] <= intervals[i][0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, (intervals[i][1], intervals[i][0], intervals[i][1]))
            ans = max(ans, len(min_heap))


        return ans