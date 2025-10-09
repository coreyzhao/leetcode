# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(101, head)
        cur = head

        while cur:
            if prev.val == cur.val:
                cur = cur.next
                prev.next = cur
            else:
                prev = prev.next
                cur = cur.next

        

        return head