
# Singly Linked Lists - Code Challenge 5
Linked List is a linear data structure.
It is a series of connected "nodes" that contains the "address" of the next node. Each node can store a data point which may be a number, a string or any other type of data.

## Author: Malak khasawneh
## pr : https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/pull/5

## Challenge
Create a Node classs and LinkedList class that will have a singly linked list properties like adding element to the beginning of the linked list, check for the existence of the elemnt in the list and print all list elements as a string

## Approach & Efficiency
for the insert() function big O(1) because we can add new element only at the beginnig of the list

for the includes() function big O(N) because I used a while loop to iterate over all  linked list elements until element won't be found

for the __str__() it is also big O(N) because I also used a while loop in my solution to iterate over the list

## API
* .insert() - takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
* .includes() - takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
* .__str__ - takes in no arguments and returns a string representing all the values in the Linked List

### Task lists

- [x] Can successfully instantiate an empty linked list
- [x] Can properly insert into the linked list
- [x] The head property will properly point to the first node in the linked list
- [x] Can properly insert multiple nodes into the linked list
- [x] Will return true when finding a value within the linked list that exists
- [x] Will return false when searching for a value in the linked list that does not exist
- [x] Can properly return a collection of all the values that exist in the linked list


_________________________________________
_________________________________________
_________________________________________

# linked-list-insertions - Code Challenge 6

## Author: Malak khasawneh
## pr : https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/pull/6


# Challenge Summary
* Write methods for the Linked List class:

* append
  * arguments: new value
  * adds a new node with the given value to the end of the list
* insert before
  * arguments: value, new value
  * adds a new node with the given new value immediately before the first node that has the value specified
* insert after
  * arguments: value, new value
  * adds a new node with the given new value immediately after the first node that has the value specified
## Whiteboard Process
![Whiteboard Solution](https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/blob/linked-list-insertions/code-challenge/linked-list/3.PNG)

![Whiteboard Solution](https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/blob/linked-list-insertions/code-challenge/linked-list/2.PNG)


![Whiteboard Solution](https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/blob/linked-list-insertions/code-challenge/linked-list/1.PNG)


## Approach & Efficiency
* Efficiency of the Big O time is O(n)
## Solution
append function
  * adds a new node with the given value to the end of the list

insert Before
  * adds a new node with the given new value immediately before the first node that has the value specified

insert After
  * adds a new node with the given new value immediately after the first node that has the value specified

### checklist
 - [x] Top-level README “Table of Contents” is updated
 - [x] README for this challenge is complete
       - [x] Summary, Description, Approach & Efficiency, Solution
       - [x] Picture of whiteboard
       - [x] Link to code
 - [x] Feature tasks for this challenge are completed
 - [x] Unit tests written and passing
       - [x] “Happy Path” - Expected outcome
       - [x] Expected failure
       - [x] Edge Case (if applicable/obvious)

_________________________________________
_________________________________________
_________________________________________

# linked-list-kth - Code Challenge 7

## Author: Malak khasawneh
## pr : 


# Challenge Summary
* Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list.## Whiteboard Process

![Whiteboard Solution]()


## Approach & Efficiency
* for the .length_() function time big O(n) space big O(1) for the .kth_from_end() function time big O(n) space big O(1)

## Solution
* kth from end
  * argument: a number, k, as a parameter.
  * Return the node’s value that is k places from the tail of the linked list.
  * You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## API
* .length_(self) - method to find the lenght of the linked list
* .kth_from_end(self, k) - method to find k-th value from the end of the linked list. In our implementation K can be positive or negative and list can be empty
