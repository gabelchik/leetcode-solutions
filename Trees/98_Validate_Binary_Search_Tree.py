from collections import deque


def valid_BST(maxi, node, mini):
    if node is None:
        return True
    if node.val >= maxi or node.val <= mini:
        return False
    return valid_BST(node.val, node.left, mini) and valid_BST(maxi, node.right, node.val)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return valid_BST(float('+inf'), root, float('-inf'))
