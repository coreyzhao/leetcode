# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        length = 0
        head_copy = head
        while head_copy:
            length += 1
            head_copy = head_copy.next

        print(length)
        head_copy = head
        for i in range(length // 2):
            head_copy = head_copy.next

        second_half_head = head_copy.next
        head_copy.next = None  

        node = None
        while second_half_head:
            temp = second_half_head.next
            second_half_head.next = node
            node = second_half_head
            second_half_head = temp
        
        first_half_head = head
        while node:
            if first_half_head.next == None:
                return
            else:
                temp1 = first_half_head.next
                temp2 = node.next
                first_half_head.next = node
                node.next = temp1


                first_half_head = temp1
                node = temp2