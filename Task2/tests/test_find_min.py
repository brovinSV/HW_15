import pytest
from Task2 import task_bts
from Task2.task_bts import Tree


@pytest.fixture

def test_find_min(bst):
    assert bst.find_min() == 1
    bst.insert(0)
    assert bst.find_min() == 0