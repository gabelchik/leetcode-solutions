class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_Node(head):
    list = []
    current_element = head
    while current_element:
        list.append(current_element.val)
        current_element = current_element.next
    print(*list)
    return

class Solution:
    def deleteNode(self, node):
        while node.next.next:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None


solution = Solution()
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
solution.deleteNode(head.next)
print_Node(head)