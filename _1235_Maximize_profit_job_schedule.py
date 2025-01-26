''' 
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
Y
ou're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs 
in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

e.g.

Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120

Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

'''

'''
Thinking process:

This is by nature a DFS problem. Each job is like a Node, including start time, end time, and profit. 
Using the top-down approach, we can first sort the job by starting time, and then at any Node i, 


'''






