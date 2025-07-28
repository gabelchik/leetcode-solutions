class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        if not list1:
            return list2

        node = result = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        if list1:
            node.next = list1
        else:
            node.next = list2

        return result.next




class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if list1 and not list2:
            return list1
        if not list1 and list2:
            return list2

        result = ListNode()
        node = result
        while list1 and list2:
            node.next = ListNode()
            node = node.next
            if list1.val <= list2.val:
                node.val = list1.val
                list1 = list1.next
            else:
                node.val = list2.val
                list2 = list2.next

        while list1:
            node.next = ListNode()
            node = node.next
            node.val = list1.val
            list1 = list1.next
        while list2:
            node.next = ListNode()
            node = node.next
            node.val = list2.val
            list2 = list2.next

        return result.next
