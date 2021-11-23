# pr : https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/pull/18

# Challenge Summary
writing a function "fizz_buzz_tree" that takes a binary tree of integers as an arguement and does "FizzBuzz" to the values in the binary tree.

## Whiteboard Process
![Whiteboard Solution](https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/blob/tree-fizz-buzz/code-challenge/tree-fizz-buzz/18.PNG)

## Approach & Efficiency
It was decided that using a helper function was going to be the best way to make these functions readable. Reference to the original BinaryTree object has to be kept during recursive traversal of the binary tree, so a tree parameter is used in the fizz_buzz_tree function. The tree parameter is never mutated during the traversal and value reassignment which is important.

The next parameter that is adjusted during traversal is the root parameter. This gives reference to the position in the stack that the function is operating on.

At each step in the binary tree, before invoking the function again, the value is reassigned to the return value from the helper fiz_buzz_func. 

Big O for this function is a factor O(n) for time. 

## Solution
Looking at every value in the binary tree, our function will determine that, if a value is evenly divisible by 3 its value will be reassigned to "Fizz". If the value is evenly divisible by 5 then its value will be reassigned to "Buzz". If the value is both evenly divisible by 3 and by 5, then its value will be reassigned to "FizzBuzz". If none of these conditions are met, then our function will reassign the integer to a string of the same value.

Example:
```
Starting Values => [2] -> [3] -> [5] -> [10] -> [15] -> [19]
After fizz_buzz_tree:
Returns => ['2'] -> ['Fizz'] -> ['Buzz'] -> ['Buzz'] -> ['FizzBuzz'] -> ['19']
```