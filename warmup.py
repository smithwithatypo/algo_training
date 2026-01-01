# Rep 1/1 - Prefix Sum


def prefix_sum(arr):
    """
    Build prefix sum array where each element is sum of all previous elements.
    arr = [1, 2, 3, 4] -> [1, 3, 6, 10]
    """
    # your code here
    pass

def test_prefix_sum():
    assert prefix_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert prefix_sum([5]) == [5]
    assert prefix_sum([1, 1, 1]) == [1, 2, 3]
    assert prefix_sum([2, -1, 3]) == [2, 1, 4]
