 ## PR: https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/pull/16
 
# Challenge Summary

Find_maximum_value : takes the binary tree (it self) as an arguement and returns the highest value contained in the tree. The entire tree is traversed in the process using an iterative level approach. The variable maximum_value is assigned to the current node's value during the traversal only if the value of that node is larger than the maximum_value.

## Whiteboard Process
![Whiteboard Solution](https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/blob/tree-max/code-challenge/tree-max/16.PNG
)


## Approach & Efficiency

method has a big O of O(n) for time. Beacuse, every node in the tree has to have its value read before the list can be returned, the time will scale the same (n). 

method differ for big O of space. 
With find_maximum_value, we are only are ever keeping track of one variable, but are adding the nodes from each level to the queue. 

## Solution

**Find_maximum_value** takes the binary tree (it self) as an arguement and returns the highest value contained in the tree. The entire tree is traversed in the process using an iterative level approach. The variable maximum_value is assigned to the current node's value during the traversal only if the value of that node is larger than the maximum_value.

```
State of a given tree:
      root: [2]
           /   \
         [7]   [5]
        /  \      \
      [2]  [6]     [9]
          /  \     /  \
        [5]  [11] [4] [20]

Expected output :
  [20]
```