class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
        
arr=[1,2,3,4,5,6,7,8,9,10] 
head=None 
tail=None 
for i in arr:
    new_node=Node(i) 
    if head==None:
        head=new_node 
        tail=new_node 
    else:
        tail.next=new_node 
        tail=new_node 
current=head 
prev=None 
while current!=None:
    new_node=current.next 
    current.next=prev 
    prev=current
    current=new_node
head=prev
current=head 
while current!=None:
    print(current.data,end="->") 
    current=current.next 
print("None")
    
    