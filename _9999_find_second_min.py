"""
1) find the minimal and second minimal values of a list 
2) find the index of minimal and second minimal values of a list 
"""

def findMinValues(x):
    # x: is a list 
    min_value, second_min_value = float('inf'), float('inf')
    for v in x:
        if v <= min_value:
            second_min_value, min_value = min_value, v    # update min value to be v, and now last min_value becomes the 2nd min value 
        elif v < second_min_value:                        # if v > min_value and v < second_min_value, then update second min value 
            second_min_value = v
    
    return min_value, second_min_value

x = [6,4,3,8,10]
print(findMinValues(x))


def findMinIndex(x):
    # x: is a list 
    min_index, second_min_index = None, None           # initially we cannot assume any index so give them None
    
    for i in range(len(x)):
        if min_index is None or x[i] <= x[min_index]:
            second_min_index, min_index = min_index, i                    # swap index 
        elif second_min_index is None or x[i] < x[second_min_index]:               
            second_min_index = i
    
    return min_index, second_min_index

x = [6,4,3,8,10]
print(findMinIndex(x))

x = [1,2,3,4,5]
print(findMinIndex(x))

