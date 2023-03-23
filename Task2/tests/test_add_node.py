import pytest
from Task2 import task_bts
from Task2.task_bts import Tree


@pytest.fixture

def bst():
    # створення бінарного дерева
    bst = Tree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(1)
    bst.insert(4)
    bst.insert(7)
    bst.insert(9)
    return bst

def test_add_node(bst):
    bst.insert(6)
    assert bst.search(6) == True
    assert bst.search(10) == False

