# Challenge Summary
Review the given pseudocode, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

Once you are done with your article, code a working, tested implementation of Quick Sort based on the pseudocode provided.

## Whiteboard Process
![Whiteboard Solution](https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/blob/Quick-Sort/code-challenge/quick-sort/lab28a.PNG)
![Whiteboard Solution](https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/blob/Quick-Sort/code-challenge/quick-sort/lab28b.PNG)

## Approach & Efficiency

write a new function called Quick_sort that take an array and sort it

that function will asure that every thing in the left of the midpoint is less then it and every thing in the right of the midpoint is bigger then it

then I will call the same function for the left and the right part

as a recursion function until the array is sorted

* Space complexity Big O(log(n))
* Time complexity Big O(n^2)

## Solution

Take a list and sort it in place.
```
before: int_list = [8,4,23,42,16,15]
$ quick_sort(int_list)
after: int_list == [4,8,15,16,23,42]
```
[Blog](https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/blob/Quick-Sort/code-challenge/quick-sort/BLOG.md)