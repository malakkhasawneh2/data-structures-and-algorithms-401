from linked_list import __version__

from linked_list.linked_list import LinkedList, Node
import pytest

def test_version():
    assert __version__ == '0.1.0'




def test_empty_list():
    newlist = LinkedList()
    expected = None
    actual = newlist.head
    assert expected == actual

def test_insert_Hi(newlist):
    expected = '{ Hi } -> { 5 } -> NULL'
    actual = newlist.__str__()
    assert expected == actual

def test_insert_to_existing(newlist):
    newlist.insert(78)
    expected = '{ 78 } -> { Hi } -> { 5 } -> NULL'
    actual = newlist.__str__()
    assert expected == actual

def test_is_includes(newlist):
    newlist = LinkedList()
    newlist.includes('Hi')
    expected = True
    actual = newlist.__eq__(newlist)
    assert expected == actual


def test_is_not_includes(newlist):
    expected = False
    actual = newlist.includes(10)
    assert expected == actual







def test_add_to_tail(newlist):
    newlist = LinkedList()
    newlist.append(88)
    newlist.append(20)
    expected ='{ 88 } -> { 20 } -> NULL'
    actual = newlist.__str__()
    assert expected == actual

def test_insert_before(newlist):
    newlist.insert_before(5,200)
    expected ='{ Hi } -> { 200 } -> { 5 } -> NULL'
    actual = newlist.__str__()
    assert expected == actual

def test_insert_after(newlist):
    newlist.append('World')
    newlist.insert_after(5,700)
    expected ='{ Hi } -> { 5 } -> { 700 } -> { World } -> NULL'
    actual = newlist.__str__()
    assert expected == actual


def test_greater_than_the_length(newlist):
    expected='not in the range'
    newlist=LinkedList()
    actual=newlist.kth_from_end(4)
    assert expected==actual


def test_the_length_of_the_list_are_the_same(newlist):
    expected='not in the range'
    newlist=LinkedList()
    actual=newlist.kth_from_end(3)
    assert expected==actual

def test_not_a_positive_integer(newlist):
    expected='negative value not allowed'
    newlist=LinkedList()
    actual=newlist.kth_from_end(-3)
    assert expected==actual

def test_of_a_size_1():
    newlist = LinkedList()
    newlist.insert(10)
    expected=10
    actual = newlist.kth_from_end(1)
    assert expected == actual

def test_happy_bath_test_k_is_not_at_end():
    newlist = LinkedList()
    newlist.insert(10)
    newlist.insert('a')
    newlist.insert(4)
    newlist.insert(5)
    newlist.insert(50)
    expected='a'
    actual = newlist.kth_from_end(1)
    assert expected == actual


def test_zip_merge():
    newlist = LinkedList()
    newlist2 = LinkedList()

    newlist.insert(5)
    newlist.insert(2)
    newlist.insert(6)
    newlist.insert(4)

    newlist2.insert(50)
    newlist2.insert(20)
    newlist2.insert(60)
    newlist2.insert(40)
    newlist.zip_list(newlist,newlist2)

    actual =newlist.__str__()
    expected ='{ 4 } -> { 40 } -> { 6 } -> { 60 } -> { 2 } -> { 20 } -> { 5 } -> { 50 } -> NULL'
    assert actual == expected

def test_zip_none():
    newlist = LinkedList()
    newlist2 = LinkedList()

    newlist.zip_list(newlist,newlist2)
    actual =newlist.__str__()
    expected = None
    assert actual == expected




@pytest.fixture
def newlist():
    newlist = LinkedList()
    newlist.insert(5)
    newlist.insert('Hi')
    return newlist