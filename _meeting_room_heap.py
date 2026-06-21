# intervals = [[0,30],[5,10],[15,20]]
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of conference rooms required.

import heapq

def minRooms(intervals):
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[0])  # just intervals.sort() default is by first element
    
    rooms = []
    for i in range(len(intervals)):
        start, end = intervals[i]

        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)

    return len(rooms)

# intervals = [[0,30],[5,10],[15,20]]
intervals = [[7,10],[2,4]]
print(minRooms(intervals))

