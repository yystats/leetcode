def mergeIntervals(intervals):
    """
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
    and return an array of the non-overlapping intervals that cover all the intervals in the input.

    Example
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    """

    # sort the intervals by start 

    intervals.sort(key = lambda x: x[0])

    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval) 
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
        
    return merged 


# example
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(mergeIntervals(intervals))



