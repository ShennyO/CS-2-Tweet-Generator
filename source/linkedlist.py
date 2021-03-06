#!python
import pdb

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)
#comment

class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) looping through all of the linked list"""
        # TODO: Loop through all nodes and count one for each
        count = 0
        current_node = self.head
        if current_node is not None:
            count +=1
            while current_node.next is not None:
                current_node = current_node.next
                count+=1
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) We have the last item's location as the tail, so we're only going through 1 item"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Append node after tail, if it exists
        #The whole point of this is so we can set the current node's next
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) we're always going to be adding to the first item, which we go through first"""
        # TODO: Create new node to hold given item
        # pdb.set_trace()
        new_node = Node(item)
        # TODO: Prepend node before head, if it exists
        if self.head is not None:
            current_head = self.head
            new_node.next = current_head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def replace(self, olditem, newitem):
        new_node = Node(newitem)
        if self.head is not None:
            current_node = self.head
            while current_node.next is not None:
                if current_node.next.data == olditem:
                    current_node.next = new_node
                else:
                    current_node = current_node.next
        #We want to traverse through the linked list, and if the current node.next is equal
        #to the old item, then we set the current node's next to the new item

    #At this point, we should have all of our list already
    def find(self, quality):
        """Return an item from this linked list satisfying the given quality."""
        """Best case running time: O(1) when we find the needed object the first time
           Worst case running time: O(n) if we have to loop through every single bucket"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        if self.head != None:
            current_node = self.head

            if quality(current_node.data):
                return current_node.data
            else:
                while current_node.next is not None:
                    current_node = current_node.next
                    if quality(current_node.data):
                        return current_node.data
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) When the item is at the front or near the front
        TODO: Worst case running time: O(n) When the item is at the end or near the end because we have to
        loop through everything"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        # pdb.set_trace()
        count = 0

        if self.head is None:
            raise ValueError('Item not found: {}'.format(item))
        find_item = self.find(lambda item_: item_ == item)
        if find_item is None:
            raise ValueError('Item not found: {}'.format(item))
        else:
            # pdb.set_trace()
            if self.head.data == item and self.head.next is not None:
                selected_node = self.head #A
                self.head = selected_node.next



            current_node = self.head

            while current_node.next is not None:

                if current_node.next.data == item:
                    next_node = current_node.next
                    if next_node == self.tail:
                        self.tail = current_node
                        current_node.next = None
                    else:
                        current_node.next = next_node.next
                else:
                    current_node = current_node.next

            if self.head == self.tail:

                if self.head.data == item:
                    self.head = None
                    self.tail = None













def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

    print('\nTesting replace:')


if __name__ == '__main__':
    test_linked_list()
