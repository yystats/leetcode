"""
You are organizing an exclusive event where each guest's attendance is tracked by their entry and exit times. 
For every guest, you are given a pair [entry, exit), indicating that this guest is present at every integer time t such that entry ≤ t < exit.

Given a list times representing the attendance intervals of all guests, your task is to find the earliest time at which the maximum number 
of guests are present simultaneously.

Return the earliest time when this maximum attendance occurs.
"""


# ideas 
# we wanna find a way to track # of person in the event, that is, basically the overlapped time window
# example: p1: [1,2) p2: [2,4) --> peak #: 1, peak time: 1 
# example: p1: [1,3); p2: [2,4) --> peak #: 2, peak time: 2
# example: p1: [1,3); p2: [4,6), p3:[5, 7) --> peak #: 2, peak time: 4

import heapq
def findPeakTime(times):
    if not times:
        return 0
    
    persons = []
    peak_time = 0
    max_count = 0

    for entry, exit in times:
        if persons and persons[0] <= entry:
            heapq.heappop(persons)
        heapq.heappush(persons, exit)

        if len(persons) > max_count:
            max_count = len(persons)
            peak_time = entry

    return peak_time

times = [[1,3],[2,4]]
print(findPeakTime(times))
