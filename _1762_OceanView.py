heights = [1,3,2,4]

def getOceanView(heights):
    
    res = []
    n = len(heights)
    max_heights =  0  # this is the key; start with a reference max heights, and keep updating it 

    for i in range(n-1, -1, -1):
        if heights[i] > max_heights:
            res.append(i)
            max_heights = heights[i]

    res.reverse()

    return res 


print(getOceanView(heights))


