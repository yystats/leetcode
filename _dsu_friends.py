"""
In a social network with n people labeled from 0 to n − 1, friendships are mutual and can be direct or connected through others. 
Friendships are given as a list connections, where each element [a, b] means person a is friends with person b.

Two people are considered to be in the same friend group if there is a sequence of direct friendships connecting them (that is, they belong to the same connected component).

Your task is to determine the number of unordered pairs of people who are not friends with each other, either directly or indirectly through other friends. 
You should count all distinct pairs (i, j) where 0 ≤ i < j < n and persons i and j are not in the same friend group.
"""

# [[0,1], [1,2], [3,4]] -> [0,1,2], [3,4] 
# [[0,4], [2,4], [3,5]] -> [0,2,4], [4,5]

# first: {0: [1], 3: [4]}
# second: {1: [0, 2], 4: {3}}

from typing import List

from pandas.core.ops import rxor

def countNonFriends(n: int, connections: List[List[int]]) -> int:
    parent = list(range(n))  # parent[0] = 0, parent[1] = 1, ...

    def find(parent: List[int], x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x] 
        return x

    def union(parent, x, y):
        rx, ry = find(parent, x), find(parent, y)
        if rx != ry:
            parent[ry] = rx

    for connection in connections:
        union(parent, connection[0], connection[1])

    groupSize = {}
    for i in range(n):
        root = find(parent, i)
        if root in groupSize:
            groupSize[root] += 1
        else:
            groupSize[root] = 1

    countFriends = 0
    for size in groupSize.values():
        countFriends += size * (size - 1) / 2
    
    total = n * (n - 1) / 2

    return total - countFriends



n = 5
connections = [[0,1], [1,2]]
print(countNonFriends(n, connections))
