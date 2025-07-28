from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_this_out(node1, node2):
            if node1 is None and node2 is None:
                return True
            if not (node1 and node2):
                return False
            if node1.val != node2.val:
                return False

            return check_this_out(node1.left, node2.right) and check_this_out(node2.left, node1.right)

        return check_this_out(root.left, root.right)


solution = Solution()
node = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
# node = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(solution.isSymmetric(node))