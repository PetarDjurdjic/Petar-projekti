class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self,head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


nodeB4 = ListNode(6, None)
nodeB3 = ListNode(1, nodeB4)
nodeB1 = ListNode(1, nodeB3)

solution = Solution()
reved = solution.reverseList(nodeB1)

printLinkedList(reved)