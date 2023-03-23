import pytest
from Task2 import task_bts
from Task2.task_bts import Tree


@pytest.fixture

def test_find_max(bst):
    assert bst.find_max() == 9
    bst.insert(10)
    assert bst.find_max() == 10