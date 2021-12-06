def merge_sort(list_of_ints):
    """
    function to prvide a merge sort on the given list, calles recursively
    """
    
    if len(list_of_ints) > 1: # list is more than one element(for sorting)

        middle_index = len(list_of_ints)//2
        left_slice = list_of_ints[:middle_index] # left half
        
        right_slice = list_of_ints[middle_index:] # right half

        merge_sort(left_slice) 

        merge_sort(right_slice) 

        merge(left_slice, right_slice, list_of_ints) # helper function to merge left and right

def merge(left, right, lst):
    """function to merge left sublist  and rightsublist to the list in proper order"""
    i, j, k = 0,0,0

    while i < len(left) and j < len(right): # Assigns values of the final list starting at index 0 (k) the values of the lesser between left and right
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    if i == len(left): 
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    else: 
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
