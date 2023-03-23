import pytest
from Task2 import task_bts
from Task2.task_bts import Tree


@pytest.fixture

def test_delete_node(bst):
    bst.delete(4)
    assert bst.search(4) == False
    assert bst.search(5) == True
    bst.delete(5)
    assert bst.search(5) == False
    assert bst.find_max() == 9