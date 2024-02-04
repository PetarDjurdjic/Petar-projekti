class Solution:
    def reverseList(self):
        prev, curr = None, self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev