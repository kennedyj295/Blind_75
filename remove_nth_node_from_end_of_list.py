class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while right and n > 0:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next