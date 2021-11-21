import pytest
from tree.tree import _Node, BinaryTree, BinarySearchTree
from tree import __version__


def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture()
def binary_search_tree_ten():
    new_tree = BinarySearchTree()
    new_tree.add(10)
    new_tree.add(5)
    new_tree.add(20)
    new_tree.add(3)
    new_tree.add(100)
    new_tree.add(1)
    new_tree.add(15)
    new_tree.add(13)
    new_tree.add(2)
    new_tree.add(90)
    return new_tree

def test_binary_search_tree_instance():
    new_tree = BinarySearchTree()
    assert new_tree.root == None

def test_binary_search_tree_add_one():
    new_tree = BinarySearchTree()
    new_tree.add(10)
    assert new_tree.root.value == 10

def test_binary_search_tree_add_three():
    new_tree = BinarySearchTree()
    new_tree.add(10)
    new_tree.add(5)
    new_tree.add(20)
    assert new_tree.root.value == 10
    assert new_tree.root.right.value == 20
    assert new_tree.root.left.value == 5

def test_binary_search_tree_add_six():
    new_tree = BinarySearchTree()
    new_tree.add(10)
    new_tree.add(5)
    new_tree.add(20)
    new_tree.add(2)
    new_tree.add(7)
    new_tree.add(25)
    assert new_tree.root.value == 10
    assert new_tree.root.right.right.value == 25
    assert new_tree.root.left.left.value == 2
    assert new_tree.root.left.right.value == 7

def test_binary_search_tree_add_ten():
    new_tree = BinarySearchTree()
    new_tree.add(10)
    new_tree.add(5)
    new_tree.add(20)
    new_tree.add(3)
    new_tree.add(100)
    new_tree.add(1)
    new_tree.add(15)
    new_tree.add(13)
    new_tree.add(2)
    new_tree.add(90)
    assert new_tree.root.value == 10
    assert new_tree.root.right.right.left.value == 90
    assert new_tree.root.left.left.left.right.value == 2

# @pytest.mark.skip()
def test_pre_order_one():
    new_tree = BinarySearchTree()
    new_tree.add(10)
    expected = [10]
    assert new_tree.pre_order(new_tree.root) == expected
# @pytest.mark.skip()
def test_pre_order_one_again():
    new_tree = BinarySearchTree()
    new_tree.add(10)
    expected = [10]
    assert new_tree.pre_order(new_tree.root) == expected
# @pytest.mark.skip()
def test_pre_order_ten(binary_search_tree_ten):
    expected = [10,5,3,1,2,20,15,13,100,90]
    assert binary_search_tree_ten.pre_order(binary_search_tree_ten.root) == expected
# @pytest.mark.skip()
def test_in_order_ten(binary_search_tree_ten):
    expected = [1,2,3,5,10,13,15,20,90,100]
    assert binary_search_tree_ten.in_order(binary_search_tree_ten.root) == expected
# @pytest.mark.skip()
def test_post_order_ten(binary_search_tree_ten):
    expected = [2,1,3,5,13,15,90,100,20,10]
    assert binary_search_tree_ten.post_order(binary_search_tree_ten.root) == expected

def test_contains_tree_of_ten(binary_search_tree_ten):
    expected = True
    assert binary_search_tree_ten.contains(10) == expected
    assert binary_search_tree_ten.contains(2) == expected
    assert binary_search_tree_ten.contains(1) == expected
    assert binary_search_tree_ten.contains(3) == expected
    assert binary_search_tree_ten.contains(5) == expected
    assert binary_search_tree_ten.contains(13) == expected
    assert binary_search_tree_ten.contains(15) == expected
    assert binary_search_tree_ten.contains(90) == expected
    assert binary_search_tree_ten.contains(100) == expected
    assert binary_search_tree_ten.contains(20) == expected
    assert binary_search_tree_ten.contains(60) == False




    ## lab 16


def test_find_max_binarytree_empty():
    tree = BinaryTree()
    assert tree.find_maximum_value() == None

def test_find_max_binarytree_one_el():
    tree = BinaryTree()
    tree.root = _Node(8)
    assert tree.find_maximum_value() == 8

def test_find_max_binarytree_several_el():
    tree = BinaryTree()
    tree.root = _Node(8)
    tree.root.left = _Node(10)
    tree.root.right = _Node(-2)
    assert tree.find_maximum_value() == 10
    tree.root.left.left = _Node(195)
    tree.root.left.right = _Node(-195)
    tree.root.right.right = _Node(10000)
    tree.root.left.left.left = _Node(-0.567)
    tree.root.left.left.right = _Node(10000)
    assert tree.find_maximum_value() == 10000

# def test_find_max_binarytree_same_values():
#     tree = BinaryTree()
#     tree.root = _Node(-2)
#     tree.root.left = _Node(-2)
#     tree.root.right = _Node(-2)
#     tree.root.left.left = _Node(-2)
#     tree.root.left.right = _Node(-2)
#     tree.root.right.right = _Node(-2)
#     tree.root.left.left.left = _Node(-2)
#     tree.root.left.left.right = _Node(-2)
#     assert tree.find_maximum_value() == -2
#     tree.root.right.left = _Node(1)
#     assert tree.find_maximum_value() == 1

def test_find_max__imbalanced_binarytree():
    tree = BinaryTree()
    tree.root = _Node(-2)
    tree.root.left = _Node(5)
    tree.root.left.left = _Node(9)
    tree.root.left.left.left = _Node(2)
    tree.root.left.left.left.left = _Node(2)
    assert tree.find_maximum_value() == 9

def test_find_max_binarytree_zeros():
    tree = BinaryTree()
    tree.root = _Node(-2)
    tree.root.left = _Node(-4)
    tree.root.right = _Node(0)
    assert tree.find_maximum_value() == 0

def test_maximum_value():
    new_tree = BinarySearchTree()
    expected = 11
    new_tree.add(2)
    new_tree.add(7)
    new_tree.add(5)
    new_tree.add(2)
    new_tree.add(6)
    new_tree.add(9)
    new_tree.add(5)
    new_tree.add(11)
    new_tree.add(4)
    assert new_tree.find_maximum_value() == expected

def test_negative_max_value():
    new_tree = BinarySearchTree()
    expected = -2
    new_tree.add(-2)
    new_tree.add(-3)
    new_tree.add(-7)
    new_tree.add(-5)
    new_tree.add(-2)
    new_tree.add(-6)
    new_tree.add(-9)
    new_tree.add(-5)
    new_tree.add(-11)
    new_tree.add(-4)
    assert new_tree.find_maximum_value() == expected