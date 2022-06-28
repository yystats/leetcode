def minMeetingRooms(intervals):
    """
    Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
    return the minimum number of conference rooms required.

    Example

    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: 2

    Idea: 
    - sort the interval by start
    - push the end into a binary heap 
    - check if the new start > heap element 0 then pop, and use the same room; else assign a new room by adding its end into the heap

    Time Complexity: O(NlogN)
    Space: O(N)
    """

    import heapq

    if not intervals:
        return 0 
    
    intervals.sort(key = lambda x: x[0])

    rooms = [intervals[0][1]]
    heapq.heapify(rooms)

    for i in range(1, len(intervals)):
        start, end = intervals[i]

        if start >= rooms[0]:
            heapq.heappop(rooms)

        heapq.heappush(rooms, end)

    return len(rooms)
            
intervals = [[0,30],[5,10],[15,20]]
print(minMeetingRooms(intervals))

