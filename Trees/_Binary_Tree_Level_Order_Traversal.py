from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        qq = deque()
        qq.append(root)
        result = []
        while qq:
            a = []
            for _ in range(len(qq)):
                node = qq.popleft()
                a.append(node.val)
                if node.left:
                    qq.append(node.left)
                if node.right:
                    qq.append(node.right)
            result.append(a)
        return result


solution = Solution()
node = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(solution.levelOrder(node))

