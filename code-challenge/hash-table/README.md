# Hashtables
Hash tables are a type of data structure in which the address or the index value of the data element is generated from a hash function. That makes accessing the data faster as the index value behaves as a key for the data value. In other words Hash table stores key-value pairs but the key is generated through a hashing function.

So the search and insertion function of a data element becomes much faster as the key values themselves become the index of the array which stores the data.

## Challenge
Implement a Hashtable with the following methods:

add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
get: takes in the key and returns the value from the table.
contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
hash: takes in an arbitrary key and returns an index in the collection.

## Approach & Efficiency
* For .hash(self, key) method time Big O(n): n = the key length, space Big O(1)
* For .add(self, key, value) method time Big O(1) , space Big O(1)
* For .get(self, key) method time Big O(1), space Big O(1)
* For .contains(self, key) method time Big O(1), space Big O(1)

## API
Three public methods for this Hash Table.
```
1. HashTable.add(key, value)
2. HashTable.get(key)
3. HashTable.contains(key)
```
Add: Takes key and value as arguements, hashes the key, returns hash-index, and adds the key/value pair to the HashTable at hash-index. Also handles collisions.

Get: Takes key as arguement, hashes key; assigns a hash-index, returns value from table at the hash-index.

Contains: Takes in a key as arguement and returns a boolean if key is already in HashTable.
