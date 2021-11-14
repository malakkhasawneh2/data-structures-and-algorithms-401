# stack-queue-pseudo / Code Challenge: Class 11

# Challenge Summary

* Build PseudoQueue class will implement our standard queue interface and add to it two method enqueue and dequeue using the Stack method pop and push

## Whiteboard Process

![Whiteboard Solution](https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/blob/stack-queue-pseudo/code-challenge/stack-queue-pseudo/d.PNG)

![Whiteboard Solution](https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/blob/stack-queue-pseudo/code-challenge/stack-queue-pseudo/e.PNG)

## Approach & Efficiency
* init(self, stack1) - initialization of the PseudoQueue class with the 1 given Stack and 1 empty Stack
* enqueue(value) - Method to inserts value into the PseudoQueue, using a first-in, first-out approach.
  * Big O :

    * time : O(1)
    * space : O(1)
* dequeue() - Method to extract a value from the PseudoQueue, using a first-in, first-out approach. Returns value of extracted node
  * Big O :

    * time : O(n)
    * space : O(1)

## Solution
**enqueue(value)**
Input: </br>
[10]->[15]->[20] </br>
Arg: </br>
5 </br>
Output: </br>
[5]->[10]->[15]->[20] </br>

Input: </br>
Empty </br>
Arg: </br>
5 </br>
Output: </br>
[5]->[ </br>

**dequeue()** </br>
Input: </br>
[5]->[10]->[15]->[20] </br>

Output: </br>
20 </br>

Internal State: </br>
[5]->[10]->[15]) </br>

## PR 
* https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/pull/12
