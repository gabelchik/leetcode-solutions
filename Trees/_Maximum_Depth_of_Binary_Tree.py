from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# С помощью рекурсии
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return 0
#         chapter_left = self.maxDepth(root.left)
#         chapter_right = self.maxDepth(root.right)
#         return max(chapter_left, chapter_right) + 1

# С помощью bfs
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = deque()
        q.append(root)
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return depth


solution = Solution()
node = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.maxDepth(node))
