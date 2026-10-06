# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        arr=[]
        curr=head 
        while curr: 
            arr.append(curr.val) 
            curr=curr.next 
        arr.sort() 
        head=None 
        tail=None 
        for i in arr:
            new_node=ListNode(i) 
            if head==None:
                head=new_node
                tail=new_node 
            else:
                tail.next=new_node
                tail=new_node 
        return head
        # curr=head 
        # while curr is not None:
        #     temp=head 
        #     while temp.next is not None:
        #         if temp.val>temp.next.val:
        #             temp.val,temp.next.val=temp.next.val,temp.val 
        #         temp=temp.next 
        #     curr=curr.next 
        # return head