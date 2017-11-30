#!python

from linkedlist import LinkedList
from linkedlist import Node
import pdb


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        #For every bucket, we will create a linked list, we already created a linkedlist class from before
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        #items is created through our items function below
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        bucket_values = []
        for bucket in self.buckets:

            #Here I have to loop through the linked list and gather all of its values
            bucket_items = bucket.items()
            for item in bucket_items:
                bucket_values.append(item[1])
        return bucket_values


    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        count = 0
        for bucket in self.buckets:
            count += bucket.length()

        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

        bucket_index = hash_and_return_index(key, self.buckets)
        selected_bucket = self.buckets[bucket_index]
        if selected_bucket.head is not None:
            if selected_bucket.find(lambda item: item[0] == key) is not None:
                return True
            else:
                return False
        else:
            return False


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        #Steps: Hash the key and find the corresponding index of our bucket array.
        # Use the find function of the linked list to iterate through that linked list
        # If it finds our key, we'll return that object[1], our object being our selected tuple

        selected_bucket = find_bucket(key, self.buckets)

        #the item is going to act as what gets passed into the find function
        #In our case, it's going to be the node's data, which is a tuple
        found_object = selected_bucket.find(lambda item: item[0] == key)
        if found_object != None:
            return found_object[1]

        raise KeyError('Key not found: {}'.format(key))


        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""

        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        # pdb.set_trace()
        new_object = (key, value)

        bucket_index = hash_and_return_index(new_object[0], self.buckets)

        selected_bucket = self.buckets[bucket_index]
        #Right now we are getting an error because we have no head.
        #so we should first check the bucket's index, and see if that linked_list has a head first, if it doesn't,
        #we know it's empty and we can jut append a new node, but if it has a head, then we can use the find method and update



        if selected_bucket.find(lambda item: item[0] == new_object[0]) is not None:
        #Now we have an error when we have to append a new object to a LinkedList
        #We also need to check if the key-value exists in the bucket, and if it does update, but if not, we append
        #At this point, we have to update that specific tuple into our new object
            found_object = selected_bucket.find(lambda item: item[0] == new_object[0])
            self.delete(found_object[0])
            selected_bucket.append(new_object)
            print(selected_bucket)
        else:
            selected_bucket.append(new_object)



    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        selected_bucket = find_bucket(key, self.buckets)
        # TODO: Check if key-value entry exists in bucket
        if selected_bucket.head is not None:
            if selected_bucket.find(lambda item: item[0] == key) is not None:
                found_object = selected_bucket.find(lambda item: item[0] == key)

                selected_bucket.delete(found_object)
            else:
                raise KeyError('Key not found: {}'.format(key))
        else:
            raise KeyError('Key not found: {}'.format(key))
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))


def find_bucket(key, buckets):
    hashed_key = hash(key)
    # pdb.set_trace()
    index = hashed_key % len(buckets)
    return buckets[index]

def hash_and_return_index(key, buckets):
    hashed_key = hash(key)
    # pdb.set_trace()
    index = hashed_key % len(buckets)
    return index

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
