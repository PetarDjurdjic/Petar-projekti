class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Array Solution

class Solution:
    def isPalindrome(self,head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l +=1
            r -=1
        return True

# Fast/Slow Pointer

class Solution:
    def isPalindrome(self,head):
        fast = head
        slow = head

        # find middle(slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

