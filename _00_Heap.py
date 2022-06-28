"""
Pirority Queue in Python
Time complexity: O(log n)
"""
import heapq 

"""
There are three functions: 
- heapify: convert a list into a binary heap
- heappush: insert a value
- heappop: pop the min value 
"""

# initializing list
li = [5, 7, 9, 1, 3]
  
# using heapify to convert list into binary heap
heapq.heapify(li)
  
# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)
  
# using heappop() to pop smallest element
print(heapq.heappop(li))   # 1
print(heapq.heappop(li))   # 3
print(heapq.heappop(li))   # 4




