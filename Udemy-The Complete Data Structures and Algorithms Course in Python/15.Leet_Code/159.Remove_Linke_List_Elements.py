class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(next = head)
        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next



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
del_Dup = solution.removeElements(nodeB1,1)

printLinkedList(del_Dup)