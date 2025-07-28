from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_Node(head):
    list = []
    while head:
        list.append(head.val)
        head = head.next
    print(*list)
    return

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        cur = head
        while cur.next:
            tmp1 = cur
            cur = cur.next
            tmp1.next = prev
            prev = tmp1
        cur.next = prev
        return cur

head = ListNode
# head = ListNode(1)
# head.next = ListNode(2)
solution = Solution()
head = solution.reverseList(head)
print_Node(head)