from linked_list import __version__

from linked_list.linked_list import LinkedList, Node
import pytest

def test_version():
    assert __version__ == '0.1.0'



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

@pytest.fixture
def newlist():
    newlist = LinkedList()
    newlist.insert(5)
    newlist.insert('Hi')
    return newlist