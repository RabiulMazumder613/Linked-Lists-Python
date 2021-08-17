from linkedLists import LinkedList, Node

#Now we create a Linked List by appending some values
my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(10)
my_linked_list.append(16)
my_linked_list.append(88)
print("Original Linked List:", end= ' ')
my_linked_list.print_list()
#1 10 16 88

def reverse(linked_list):
    # if the linked list is empty or has just one node
    # then just return the list as there is nothing to reverse
    if linked_list.length <=1:
        return linked_list
    else:
        # create two nodes first and second which point to 
        # the first and second nodes of the list respectively
        first = linked_list.head
        second = first.next
        #Then we update the tail of the list to point to the head 
        # as after reversing the present head will become the last node
        linked_list.tail = linked_list.head 
        while second is not None: # As long as second isn't Null run the code below
            temp = second.next # temp node which points to the 'next' of the second node
            second.next = first
            first = second
            second = temp
        linked_list.head.next = None # The head is 1 and now it points to null/None
        linked_list.head = first # The head is now first(which is 88)
        return linked_list

reversed_linked_list = reverse(my_linked_list)
print("\nReversed Linked List:", end= ' ')
reversed_linked_list.print_list()
#88 16 10 1