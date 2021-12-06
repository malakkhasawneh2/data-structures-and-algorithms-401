from merge_sort import __version__
import pytest
from merge_sort.merge_sort import merge_sort


def test_version():
    assert __version__ == '0.1.0'



def test_merge_sort_simple():
    lst = [1,2,3,9,4,5]
    merge_sort(lst)
    assert lst == [1, 2, 3, 4, 5, 9]

def test_blog_merge_sort():
    lst = [8,4,23,42,16,15]
    merge_sort(lst)
    assert lst == [4, 8, 15, 16, 23, 42]

def test_reverse_sorted_merge_sort():
    lst = [20,18,12,8,5,-2]
    merge_sort(lst)
    assert lst == [-2, 5, 8, 12, 18, 20]

def test_few_uniques_merge_sort():
    lst = [5,12,7,5,5,7]
    merge_sort(lst)
    assert lst == [5, 5, 5, 7, 7, 12]

def test_nearly_sorted_merge_sort():
    lst = [2,3,5,7,13,11]
    merge_sort(lst)
    assert lst == [2, 3, 5, 7, 11, 13]

def test_large_list_merge_sort():
    lst = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48,71,-2,-60,16,40,8]
    merge_sort(lst)
    assert lst == [-60, -2, 2, 3, 4, 5, 8, 15, 16, 19, 26, 27, 36, 38, 40, 44, 46, 47, 48, 50, 71]

def test_empty_list_merge_sort():    
    lst = []
    merge_sort(lst)
    assert lst == []