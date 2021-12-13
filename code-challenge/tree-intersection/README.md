# Challenge Summary
This challenge asks us to write a function that takes two strings as arguments and returns a list of the elements that both trees have in common.

Traverse both trees keeping track of the values in each. Return a list of the elements that they have in common.
```
State of a given tree_one:      State of a given tree_two:
      root: [150]                         root:   [42]                           
           /   \                               /       \
         [100]   [250]                       [100]     [600]
        /  \      \                         /  \        /  \
      [75]  [160][350]                    [15]  [160] [200][350]
           /  \     /  \                          /  \       / \
        [125][175][300][500]                    [125][175] [4] [500]
```
```Output: [100,160,125,175,200,350,500]```
## Whiteboard Process
### i explane the big o in Approach & Efficiency
![Whiteboard Solution](https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/blob/tree-intersection/code-challenge/tree-intersection/lab32a.PNG)
![Whiteboard Solution](https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/blob/tree-intersection/code-challenge/tree-intersection/labb32.PNG)

## Approach & Efficiency
a hash table has O(1) time complexity to check. As apposed another O(n) implication with a list.

We are passing a boolean into the tree_intersection recursive helper function that tells it when to check a conditional. After all of the nodes in tree one are checked and their values are added to our hash table, then we pass in True. True gets passed throughout the recursive traversal and checks if the node values are included in the hash table.

The efficency here breaks down to is O(N) for time (all nodes) and O(N) for space. The O(1) for time using a hash table to check if any value is included saves us here. As if the lookup was not O(1) we would be looking at at least O(n^2) for time.

## Solution
```
State of a given tree_one:      State of a given tree_two:
      root: [150]                         root:   [42]                           
           /   \                               /       \
         [100]   [250]                       [100]     [600]
        /  \      \                         /  \        /  \
      [75]  [160][350]                    [15]  [160] [200][350]
           /  \     /  \                          /  \       / \
        [125][175][300][500]                    [125][175] [4] [500]
```
```Output: [100,160,125,175,200,350,500]```
