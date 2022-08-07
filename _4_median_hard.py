"""
4. Median of Two Sorted Arrays [Hard]

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Reference: https://www.youtube.com/watch?v=LPFhl65R7ww&t=1327s

Time: O(log(min(len(x)), min(len(y))))

"""

def findMedian(x, y):

    """
    idea: 
     - do a partition to x, and another partition to y, and ensure that len(left partition x) + len(left partition y) = len(right partition x) + len(right partition y), 
     - only include 1 more element in the left for x + y is odd case 
     - then we need to maxLeftX vs minRightY, and maxLeftY vs minRightX -- this moves the pointers 
    """

    if len(y) < len(x):
        return findMedian(y, x)
        
    start, end = 0, len(x)
    
    while start <= end:
        partition_x = (start + end) // 2
        partition_y = (len(x) + len(y) + 1) // 2 - partition_x   # plus 1 to ensure that left partition Y contains 1 more element when x + y is odd number

        # if partition at index = 0 then no more in the left 
        # if partition at index = len(x) then no more in the right 
        # the partition index is contained in the right 

        maxLeftX = -float('inf') if partition_x == 0 else x[partition_x - 1]
        minRightX = float('inf') if partition_x == len(x) else x[partition_x]
        
        maxLeftY = -float('inf') if partition_y == 0 else y[partition_y - 1]
        minRightY = float('inf') if partition_y == len(y) else y[partition_y]
        
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (len(x) + len(y)) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            end = partition_x - 1
        elif maxLeftY > minRightX:
            start = partition_x + 1
    
x = [1,3,8,9,15]
y = [7,11,18,19,21,25]
print(findMedian(x, y)) ## 11


x = [23,26,31,35,37,50,60]
y = [3,5,7,9,11,16]
print(findMedian(x, y)) ## 23

x = [1,3]
y = [2]
print(findMedian(x, y)) ## 2

