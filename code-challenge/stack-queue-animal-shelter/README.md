# PR :  
# Challenge Summary
* Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
Implement the following methods:

  * enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
  * dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return None.

## Whiteboard Process
![Whiteboard Solution]()


## Approach & Efficiency
* For the enqueue(animal) method time big O(1), space big O(1) For the dequeue(pref) method time big O(n), space big O(n)

## Solution

**enqueue(value)**
Internal state before: </br>
[cat2]->[dog1]->[cat1] </br>
Input </br>
"dog3", "dog"
Internal state after: </br>
[dog3]->[cat2]->[dog1]->[cat1] </br>