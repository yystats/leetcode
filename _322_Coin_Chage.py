"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""

def findMinCoins(coins, amount):
    """
    This is a DP problem. Key logic:

    dp[i] = min(dp[i], dp[i-c] + 1) for all coins c 
    - dp[i] stores the min coins needed that their values adds to i 
    - at dp[i], if we plan to use any coin, we need to find the min coins needed at dp[i-c]
    - we need to get the min across all coins  
    """

    dp = [float('inf')] * (amount + 1)
    trace = [0] * (amount + 1) # save the coins used at each smaller amount
    dp[0] = 0

    for i in range(1, amount + 1):
        for j in range(len(coins)):
            c = coins[j]
            if c <= i and dp[i-c] + 1 <= dp[i]:
                dp[i] = dp[i-c] + 1
                trace[i] = j

    # back-tracing the coins used 
    coins_used = []

    if dp[amount] != float('inf'):
        numCoins = dp[amount]
        index = len(trace) - 1

        while numCoins > 0:
            coins_used.append(trace[index])
            index -= coins[trace[index]]
            numCoins -= 1

    return (dp[amount], coins_used) if dp[amount] != float('inf') else (-1, None)


coins = [1,2,5]
amount = 11
print(findMinCoins(coins, amount))



