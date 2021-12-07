## Quick Sort


## Pseudocode

```
 ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp

```

## Trace
#### Sample array: [8,4,23,42,16,15]

### Pass 1
We are calling a quick_sort tfunction passing our list, 0(first index in list) and 5(last index in list) as a parameters.

Inside of our quick_sort function we are calling partition function(last, 0, 5).
The last element of the list with index 5 becomes a pivot. Then we put all elements less than 15 to the left of the list, and all element more than 15 to the right of the list.


### Pass 2

We are calling quick_sort function recursively on the left and right parts of the list.



### Pass 3

Inside of each quick_sort() function call we are having a call of partition function.


### Pass 4
When we finish iterating in partition we invoke swap.


#### Sorted array: [4, 8, 15, 16, 23, 42]

## Efficiency
* Space complexity Big O(log(n))
* Time complexity Big O(n^2)
