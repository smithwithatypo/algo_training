# Rep 1/1 - Contains Duplicate


def contains_duplicate(nums):
    """
    Return True if any value appears at least twice in the array.
    nums = [1, 2, 3, 1] -> True
    nums = [1, 2, 3, 4] -> False
    """
    # your code here
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False
    pass

def test_contains_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) == True
    assert contains_duplicate([1, 2, 3, 4]) == False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    assert contains_duplicate([]) == False
    assert contains_duplicate([1]) == False
