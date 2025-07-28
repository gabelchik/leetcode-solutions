from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def valid_BST(maxi, node, mini):
    if node is None:
        return True
    if node.val >= maxi or node.val <= mini:
        return False
    return valid_BST(node.val, node.left, mini) and valid_BST(maxi, node.right, node.val)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return valid_BST(float('+inf'), root, float('-inf'))



solution = Solution()
node = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
print(solution.isValidBST(node))