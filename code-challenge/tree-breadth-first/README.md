## Breadth-first Traversal.
## PR: 

# Challenge Summary

takes the binary tree of nodes (its self) as an arguement and returns a list of the values inside of those nodes; starting from the root and stretching the width of the tree left to right and top to bottom. 

## Whiteboard Process
![Whiteboard Solution]()

## Approach & Efficiency

As nodes get removed from the queue, and their children are added, eventually the final "level" of the tree will be reached. Meaning to say that there are no further children, no further levels. So the nodes will be dequeued like normal and when the queue is empty, that is when we can return our list of values.

a big O of O(n) for time. Beacuse, every node in the tree has to have its value read before the list can be returned, the time will scale the same (n). 

breadth_first method it will have O(n)
 
## Solution

**Breadth_first** takes the binary tree of nodes (its self) as an arguement and returns a list of the values inside of those nodes; starting from the root and stretching the width of the tree left to right and top to bottom. 

That is what "breadth first" is describing. The breadth of the tree starting at the top, going from left to right. First. Meaning before going to the next "level" in the height of the binary tree. Here is an example:
```
State of a given tree:
      root: [2]
           /   \
         [7]   [5]
        /  \      \
      [2]  [6]     [9]
          /  \     /
        [5]  [11] [4]

Expected output from breadth_first method:
  [2, 7, 5, 2, 6, 9, 5, 11, 4]
```
As you can see, the method is reading the value of each of the nodes in the tree, starting with the root's level, moving to the next level (7 and 5 -- left to right), then moving farther down to the next level (2, 6, and 9), and after that level we reach the final level (5, then 11, then 4).

This is traversing a Binary Tree **breadth first**.