class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# First linked list: 1 -> 5 -> 3
head1 = Node(1)
head1.next = Node(5)
head1.next.next = Node(3)

# Second linked list: 4 -> 2 -> 6
head2 = Node(4)
head2.next = Node(2)
head2.next.next = Node(6)


# Function to print a linked list
def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


# Step 1: Convert linked list to an array,
# sort the array, and rebuild the linked list
def sort_list(head):
    arr = []
    curr = head

    while curr is not None:
        arr.append(curr.data)
        curr = curr.next

    arr.sort()

    new_head = None
    tail = None

    for value in arr:
        new_node = Node(value)

        if new_head is None:
            new_head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    head1 = sort_list(head1)
    head2 = sort_list(head2)

    print_list(head1)
    print_list(head2)

    
