# Rep 1/1 - Recursion


def factorial(n):
    """
    Calculate factorial using recursion.
    factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
    """
    # your code here - must use recursion
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n-1)
    pass

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(3) == 6
