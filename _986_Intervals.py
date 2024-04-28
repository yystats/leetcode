
def intervalIntersection(firstList, secondList):
    """
    Key idea: use two pointers 
    For overlapping at one single point, do not overthink, as long as 
    they have overlap, we can use max(), and min() to find the left and the right 

    first = [[0,2], [3,5]]
    second = [[2,3]]

    """

    if not firstList or not secondList:
        return []
    
    p1 = p2 = 0 
    res = []

    while p1 < len(firstList) and p2 < len(secondList):
        start1, end1 = firstList[p1]
        start2, end2 = secondList[p2]

        if start1 > end2:
            p2 += 1
        elif start2 > end1:
            p1 += 1
        else:
            res.append([max(start1, start2), min(end1, end2)])
            if end1 > end2:
                p2 += 1
            else:
                p1 += 1

    return res


firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
print(intervalIntersection(firstList, secondList))

