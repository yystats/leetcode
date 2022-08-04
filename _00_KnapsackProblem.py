"""
Knapsack Problem 

Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack

w = [w1, w2, ..., wn]
v = [v1, v2, ..., vn] 

maximize sum V_i
subject to sum wi <= W

1) 0-1 knapsack problem: an item can only be used once 
2) unbounded knapsack problem: an item can be repetitively used

Dynamic Programing:

For 0-1:

1) create an (n+1) x (W + 1) matrix V, which stores the max value up to row i and column w 
    - rows: items used up to i 
    - cols: capacity weight up to w
2) initialize base case
    - V[0,] = 0 -- no items were used just return 0 
3) key logic:
    - V[i, w] = max(V[i-1, w], v_i + V[i-1, w-w_i])  when w_i <= w
    - V[i, w] = V[i-1, w]  when w_i > w


For unbounded:
In the 0-1 case, we use i to track items used up to i; however, since an item can be repeated used, we no longer need the i to track items used 

1) create an array with length W + 1: dp[]
2) initialized dp[0] = 0
3) dp[w] = max(dp[w], v_i + dp[w-w_i])   for all i in items

"""

def knapsack_01(w, v, W):
    n = len(v)
    V = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                V[i][j] = 0
            elif w[i-1] <= j:
                V[i][j] = max(V[i-1][j], v[i-1] + V[i-1][j-w[i-1]])
            else:
                V[i][j] = V[i-1][j]

    return V[n][W]


def knapsack_unbounded(w, v, W):
    n = len(v)
    dp = [0] * (W + 1)
    
    for wt in range(1, W + 1):
        for j in range(n):
            if w[j] <= wt:
                dp[wt] = max(dp[wt], v[j] + dp[wt-w[j]]) 

    return dp[W]


v = [60,100,120]
w = [10,20,30]
W = 50

print(knapsack_01(w, v, W))

v = [10, 40, 50, 70]
w = [1, 3, 4, 5]
W = 8

print(knapsack_unbounded(w, v, W))




