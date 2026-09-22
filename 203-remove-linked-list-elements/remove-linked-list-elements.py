# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        while head!=None and head.val==val:
            head=head.next
        previous=None 
        current=head 
        while current!=None:
            if current.val==val:
                previous.next=current.next 
            else:
                previous=current 
            current=current.next
        return head