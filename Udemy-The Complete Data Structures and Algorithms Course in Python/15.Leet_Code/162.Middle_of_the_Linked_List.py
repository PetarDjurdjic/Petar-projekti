class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
        return head


def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


nodeB4 = ListNode(6, None)
nodeB3 = ListNode(5, nodeB4)
nodeB1 = ListNode(1, nodeB3)

solution = Solution()
mid = solution.middleNode(nodeB1)

printLinkedList(mid)