## Merge Sort
Merge sort breaks a list up into the smaller lists than merges the lists back together in order.

* Merge sorts a fast but require a big amount of memory.
* Merge Sort is useful for sorting linked lists.
* Merge Sort is a stable sort which means that the same element in an array maintain their original positions with respect to each other.

To sort a sequence S with n elements using the three divide-and-conquer steps, the merge-sort algorithm proceeds as follows:
1. Divide: If S has zero or one element, return S immediately; it is already sorted. Otherwise (S has at least two elements), remove all the elements from S and put them into two sequences, S1 and S2, each containing about half of the elements of S; that is, S1 contains the first [n/2] elements of S, and S2 contains the remaining [n/2] elements.
2. Conquer: Recursively sort sequences S1 and S2.
3. Combine: Put back the elements into S by merging the sorted sequences S1
and S2 into a sorted sequence.

## Pseudocode

```
 ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

```

## Trace
#### Sample array: [8,4,23,42,16,15]

### Pass 1

Our function merge sort recursivly devides our list by half, than its left and right part on half and so on. at the same time inside each mege_sort() function call we are calling merge() function and passing to it the current left, right, and part of the list. The merge() function should merge in proper order all element from left and right sequences.



### Pass 2

Our merge(left, right, lst) function will start form the bottom of our "tree". [4] will be left list, [23] right list, [4, 23] the lst.
After merging 4 and 23, our lst stays [4, 23]



### Pass 3

Again merge() will be called with ([8], [4, 23], [8, 4, 23]) as parameters. After merging our lst became [4, 8, 23]


### Pass 4

Now merge() finished with the left part of our "tree" and goes to the right branches.
Merge will be called with ([16], [15], [16, 15]) as parameters. After merging our lst became [15, 16]


### Pass 5

Merge will be called with ([42], [15, 16], [42, 16, 15]) as parameters. After merging and proper ordering our lst became [15, 16, 42]

### Pass 6

Now our "tree" has two ordered sublists. Call merge last tme with this sublists and our list as parameters. Our lists merged and all elements are ordered.



#### Sorted array: [4, 8, 15, 16, 23, 42]

## Efficiency
* Space complexity Big O(n)
* Time complexity Big O(nLogn)
