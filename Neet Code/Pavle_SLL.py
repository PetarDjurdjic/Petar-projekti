class ListNode(object):
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def merge_lists(nodeA, nodeB):
    currA = nodeA
    currB = nodeB
    print("List A = ")
    while currA:
        print(currA.val)
        currA = currA.next
    print("\nList B = ")
    while currB:
        print(currB.val)
        currB = currB.next
    print("\n")

# List A
nodeA4 = ListNode(4, None)
nodeA2 = ListNode(2, nodeA4)
nodeA1 = ListNode(1, nodeA2)

# List B
nodeB4 = ListNode(4, None)
nodeB3 = ListNode(3, nodeB4)
nodeB1 = ListNode(1, nodeB3)

merge_lists(nodeA1, nodeB1)
