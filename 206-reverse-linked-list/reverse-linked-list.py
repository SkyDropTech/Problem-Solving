# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr=head 
        previous=None 
        while curr!=None:
            next_node=curr.next 
            curr.next=previous 
            previous=curr 
            curr=next_node
        return previous