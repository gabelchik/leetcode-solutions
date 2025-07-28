from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_Node(head):
    list = []
    current_element = head
    while current_element:
        list.append(current_element.val)
        current_element = current_element.next
    print(*list)
    return


# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         last = head
#         k = 1
#         while last.next:
#             k+=1
#             last = last.next
#         k = k - n
#
#         if k == 0:
#             return head.next
#
#         tmp1 = head
#         t = 1
#         while t != k:
#             t+=1
#             tmp1 = tmp1.next
#         tmp1.next = tmp1.next.next
#         return head

# Через один проход:
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head = solution.removeNthFromEnd(head, 5)
print_Node(head)
