import re

def display_hash(hashtable) -> None:
	# Write your code here

def Hashing(keyvalue) -> int:
	return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value) -> None:
	# Write your code here


# Do not edit the following code
hash_table_size = int(input())
# Create Hashtable as a list of list.
HashTable = [[] for _ in range(hash_table_size)]
input_data = input()
data = []
for item in re.split('], |].', input_data):
  item = item[1:]
  data = item.split(', ')
  if len(data) > 1:
    insert(HashTable, int(data[0]), data[1])

display_hash (HashTable)
