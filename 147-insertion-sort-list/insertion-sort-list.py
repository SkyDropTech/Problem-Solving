# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        curr=head 
        while curr is not None:
            temp=head
            while temp.next is not None: 
                if temp.val>temp.next.val:
                    temp.val,temp.next.val=temp.next.val,temp.val 
                temp=temp.next 
            curr=curr.next 
        return head

        