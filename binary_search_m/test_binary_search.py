import pytest
from binary_search_m.binary_search import binary_search

''' Answer

def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

'''


def test_binary_search_empty_array():
    assert binary_search([], 1) == -1

def test_binary_search_single_element_array():
    assert binary_search([1], 1) == 0
    assert binary_search([1], 2) == -1

def test_binary_search_multiple_elements():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    assert binary_search([1, 2, 3, 4, 5], 6) == -1

def test_binary_search_duplicate_elements():
    assert binary_search([1, 2, 2, 2, 3], 2) in [1, 2, 3]

def test_binary_search_negative_numbers():
    assert binary_search([-5, -4, -3, -2, -1], -3) == 2
    assert binary_search([-5, -4, -3, -2, -1], 0) == -1

def test_binary_search_large_numbers():
    assert binary_search([10**5, 10**6, 10**7], 10**6) == 1
    assert binary_search([10**5, 10**6, 10**7], 10**8) == -1

if __name__ == "__main__":
    pytest.main()
