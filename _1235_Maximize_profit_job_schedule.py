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

Using the top-down approach, we can first sort the job by starting time, and then at any Node i, the max profit only have two scenarios:
1) scenario 1 - include this Node, so does the proift; and find the next Node (j) that start time >= current Node end time 
2) scenario 2 - does not include this Node, and basically we start with next Node (i+1)

So the max profit is just max(scenarion1, scenario2)

For scenario 1 - finding next Node is a binary search as the start time is an increasing list. We can use bisect_left to find the index. 

In addition, DFS can be enhanced with memorization, so we can store the value in a dictionary for speeding up. 

'''

from bisect import bisect_left

def jobSchedule(startTime, endTime, profit):
    # sort by start time
    jobs = list(zip(startTime, endTime, profit))
    jobs.sort()
    startTime.sort()
    
    n = len(jobs)
    memo = {} # memorize the intermediate values in the dfs for speeding up 
    
    def dfs(i):
        if i == n: return 0
        if i in memo: return memo[i]
        
        s, e, p = jobs[i] # current job 

        # we have two scenarios
        # 1) include current ith profit + the following job that does not overlap with the current one  
        # 2) does not include current ith profit, and start with the (i+1)th job
        # 3) choose the max of the two scenarios 

        j = bisect_left(startTime, e)
        s1 = p + dfs(j)
        s2 = dfs(i+1)
        memo[i] = max(s1, s2)

        return memo[i]

    return dfs(0)






