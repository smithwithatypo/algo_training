# Rep 4/4 - Binary Search


def binary_search(arr, target):
    """
    Find target in sorted array. Return index or -1 if not found.
    arr = [1,3,5,7,9], target = 5 -> return 2
    """
    # your code here
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
    pass


def test_binary_search():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search([1, 3, 5, 7, 9], 1) == 0
    assert binary_search([1, 3, 5, 7, 9], 9) == 4
    assert binary_search([1, 3, 5, 7, 9], 4) == -1
    assert binary_search([], 1) == -1
