class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


nodeB4 = ListNode(4, None)
nodeB3 = ListNode(1, nodeB4)
nodeB1 = ListNode(1, nodeB3)

solution = Solution()
del_Dup = solution.deleteDuplicates(nodeB1)

printLinkedList(del_Dup)
