from collections import deque


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
