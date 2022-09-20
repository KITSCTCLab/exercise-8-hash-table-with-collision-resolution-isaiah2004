import re

class Node:
    """
    Provide necessary documentaion
        data=store associated data
        next=link to next node
    """

    def __init__(self, data=None,name=None, next=None):
        """
        Initializes the Node with the given attributes
        """
        self.data = data
        self.name = name
        self.next = next

class LinkedList:
    """
    This class implements LinkedList using Node objects
    Methods:
        insert_at_end-inserts node with data at the end of the list
        status-displays all elements of the list
    Attributes:
        self.head-contains first node of LinkedList and None if list empty
    """

    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data, name):
        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """
        new = Node(data, name)
        current = self.head
        if current is None:
            self.head = new
        else:
            while current.next is not None:
                current = current.next
            current.next = new

    def status(self):
        """
        It prints all the elements of list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.name)
            current = current.next
        #print(elements)
        for i in range (len(elements)):
            print("'"+elements[i]+"'",end="")
            if(i<len(elements)-1):
                print(" --> ", end="")
        print()
     

def display_hash(hashtable) -> None:
	for i in range(len(hashTable)):
        print(str(i)+" --> ", end="")
        hashTable[i].status()

def Hashing(keyvalue) -> int:
	return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value) -> None:
	# Write your code here
    i = Hashing(keyvalue)
    Hashtable[i].insert_at_end(keyvalue,value)


hash_table_size = int(input())

HashTable = [LinkedList() for _ in range(hash_table_size)]
input_data = input()
data = []
for item in re.split('], |].', input_data):
  item = item[1:]
  data = item.split(', ')
  if len(data) > 1:
    insert(HashTable, int(data[0]), data[1])

display_hash (HashTable)
