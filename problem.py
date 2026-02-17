# Rep 1/1 - Stack


def valid_parentheses(s):
    """
    Check if parentheses are valid using a stack.
    "()" -> True, "()[]{}" -> True, "(]" -> False
    """
    # your code here
    pairs = {')': '(', ']': '[', '}': '{'}
    pass

def test_valid_parentheses():
    assert valid_parentheses("()") == True
    assert valid_parentheses("()[]{}")== True
    assert valid_parentheses("(]") == False
    assert valid_parentheses("([)]") == False
    assert valid_parentheses("") == True
