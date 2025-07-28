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
