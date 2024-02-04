class ListNode(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Solution(object):
    def mergeTwoLists(self, L1, L2):
        prehead = ListNode(None)
        prev = prehead

        while L1 and L2:
            if L1.value <= L2.value:
                prev.next = L1
                L1 = L1.next
            else:
                prev.next = L2
                L2 = L2.next
            prev = prev.next

        if L1 is not None:
            prev.next =L1
        else:
            prev.next = L2

        return prehead.next

nodeA4 = ListNode(4, None)
nodeA2 = ListNode(2, nodeA4)
nodeA1 = ListNode(1, nodeA2)

# List B
nodeB4 = ListNode(4, None)
nodeB3 = ListNode(3, nodeB4)
nodeB1 = ListNode(1, nodeB3)



solution = Solution()

merged_list=solution.mergeTwoLists(nodeA1, nodeB1)
while merged_list:
    print(merged_list.value, end=" ")
    merged_list = merged_list.next