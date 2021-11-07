
# Singly Linked Lists
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



_________________________________________
_________________________________________
_________________________________________

# linked-list-insertions

## Author: Malak khasawneh
## pr : 


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
![Whiteboard Solution]()

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

