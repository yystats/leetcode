# disjoint set union
class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False # do not union them as they are already connected 
        
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# example of logic #19-23
#    0
#   / \
#  1   2
#  |
#  3
#  Now if we wanna union (9, 0) - For 9: the root is 9, rank = 0; for 0: root is 0, rank = 3 -> rx = 9, ry = 0
#  so switch and rx = 0, ry = 9 -> attach 9 to 0 
#      0
#   /  |  \
#  1   2   9
#  |
#  3


# example 
network = DSU(4)
print("Connection 0 and 1 ...")
network.union(0, 1)

print("Connection 1 and 2 ...")
network.union(1, 2)

if network.connected(0, 2):
    print("Yes! 0 and 2 are in the same friend circle.")
else:
    print("No, 0 and 2 don't know each other.")
