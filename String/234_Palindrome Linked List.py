from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node, stack = head, []
        while node:
            stack.append(node.val)
            node = node.next
        node = head
        while stack:
            if stack.pop() != node.val:
                return False
            node = node.next
        return True
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         half, end = head, head
#         while end and end.next:
#             half = half.next
#             end = end.next.next
#
#         past, cur = None, half
#         while cur:
#             tmp = cur.next
#             cur.next = past
#             past = cur
#             cur = tmp
#
#         first = head
#         while past:
#             if first.val != past.val:
#                 return False
#             past = past.next
#             first = first.next
#         return True


solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
print(solution.isPalindrome(head))