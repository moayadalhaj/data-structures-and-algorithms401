from tree_fizz_buzz import __version__
from tree_fizz_buzz import *
import pytest
def test_version():
    assert __version__ == '0.1.0'

def test_empty_k_ary_tree():
    new_tree = k_ary_tree()
    assert fizz_buzz_tree(new_tree) == None


def test_filled_fizz_buzz_tree(k_arr):
    tree = fizz_buzz_tree(k_arr)
    # for the new tree
    assert tree.root.value == 'Fizz'
    assert tree.root.children[0].value == '2'
    assert tree.root.children[1].value == 'Buzz'
    assert tree.root.children[2].value == 'FizzBuzz'
    assert tree.root.children[0].children[0].value == '4'
    assert tree.root.children[0].children[1].value == 'Fizz'
    assert tree.root.children[0].children[2].value == '7'
    assert tree.root.children[1].children[0].value == 'Fizz'
    assert tree.root.children[1].children[1].value == 'Fizz'
    assert tree.root.children[2].children[0].value == 'FizzBuzz'

@pytest.fixture
def k_arr():
    tree = k_ary_tree()
    tree.root = Node(3)
    tree.root.children.append(Node(2))
    tree.root.children.append(Node(5))
    tree.root.children.append(Node(15))
    tree.root.children[0].children.append(Node(4))
    tree.root.children[0].children.append(Node(6))
    tree.root.children[0].children.append(Node(7))
    tree.root.children[1].children.append(Node(9))
    tree.root.children[1].children.append(Node(30)))
    return tree