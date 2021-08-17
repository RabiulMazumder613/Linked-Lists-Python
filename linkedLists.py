# Helpful Link for Linked Lists: https://www.educative.io/edpresso/how-to-create-a-linked-list-in-python
# # A single node of a singly linked list
# class Node:
#     # constructor
#     def __init__(self, val, next=None): 
#         self.val = val 
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = self.head
#         self.length = 1
        
# myLinkedList = LinkedList()
# myLinkedList.head = Node(3)
# print(myLinkedList.head.val)

class Node():
    def __init__(self, data, next=None):
        self.data = data #Stores the value of the node
        self.next = next # Pointer (or Reference) to the next node

# Start off with an empty Linked List
# Since there is no node to point to Head will point to None.
# Since the list is empty at the time of creation, 
# we will point the tail to whatever the head is pointing to, i.e., None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
        
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            # Whatever the tail is now pointing to is now pointing to the new_node instead
            self.tail.next = new_node
            self.tail = new_node # The tail is now new_node
            self.length += 1
        
    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            # The new node created is now pointing to the head
            new_node.next = self.head
            self.head = new_node # The head is now new_node
            self.length += 1

    def insert(self, position, data):
        if position >= self.length:
            if position>self.length:
                print("This position is not available. Inserting at the end of the list")
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        elif position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            new_node = Node(data)
            current_node = self.head # Create a new node which will point to the head.
            # We have to traverse the Linked List for the position we want since there is no 
            # reference to it. We only have a reference to the head and tail
            # Get the node before the position we want as we want the before node to point to the new node o it is at the postition we want
            for i in range(position-1): # Traverses the list to get the node that is at the position before the node we want 
                current_node = current_node.next
            new_node.next = current_node.next # The new_node now points to the node that current_node is pointing to 
            current_node.next = new_node # The node that current_node is pointing to is now the new_node
            self.length += 1


    def delete_by_position(self, position):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        if position == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        if position>=self.length:
            position = self.length-1
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        self.length -= 1
        if current_node.next == None:
            self.tail = current_node
        return

    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head # Create a new node which will point to the head.
            # Then we will loop until the node we created becomes None
            while current_node!= None:
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()
        
if __name__ == '__main__':

    my_linked_list = LinkedList()
    # my_linked_list.head = Node(10)
    # # my_linked_list.print_list()
    my_linked_list.append(10)
    my_linked_list.append(5)
    my_linked_list.append(16)
    my_linked_list.append(99)
    my_linked_list.print_list()
    my_linked_list.prepend(1)
    my_linked_list.print_list()
    my_linked_list.insert(2,69)
    my_linked_list.print_list()
    my_linked_list.insert(20,88)
    my_linked_list.print_list()
    my_linked_list.delete_by_position(2)
    # print(my_linked_list.length)
    my_linked_list.print_list()