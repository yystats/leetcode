from dataclasses import dataclass
from typing import Optional

@dataclass
class TreeNode:
    val: int
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None

class Solution:
    def get_diameter(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self._get_height(root)
        return self.diameter
    
    def _get_height(self, node):
        if not node:
            return 0
        
        left = self._get_height(node.left)
        right = self._get_height(node.right)

        self.diameter = max(self.diameter, left + right)

        return 1 + max(left, right)


# --- Example Usage ---

# Constructing your tree:
#       Root
#      /    \
#     A      B
#    / \
#   C   D
#  /     \
# E       F

tree = TreeNode(1, 
           left=TreeNode(2, # Node A
                    left=TreeNode(4, left=TreeNode(6)), # Node C & E
                    right=TreeNode(5, right=TreeNode(7)) # Node D & F
                ),
           right=TreeNode(3) # Node B
       )

sol = Solution()
print(f"The diameter of the tree is: {sol.get_diameter(tree)}")
# Output: 4 (Path: 6 -> 4 -> 2 -> 5 -> 7)


# manual test







