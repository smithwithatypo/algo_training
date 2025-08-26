# Rep 2/2 - Contains Duplicate


def contains_duplicate(nums):
    """
    Check if array contains any duplicate values.
    [1,2,3,1] -> True, [1,2,3,4] -> False
    """
    # your code here
    s = set()
    for num in nums:
        if num in s:
            return True
        else:
            s.add(num)

    return False
    pass

def test_contains_duplicate():
    assert contains_duplicate([1,2,3,1]) == True
    assert contains_duplicate([1,2,3,4]) == False
    assert contains_duplicate([1,1,1,3,3,4,3,2,4,2]) == True
    assert contains_duplicate([]) == False
    assert contains_duplicate([1]) == False
