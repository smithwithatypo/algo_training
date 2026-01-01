EXERCISES = {
    "two_pointers": {
        "title": "Two Pointers",
        "template": '''def two_sum_sorted(arr, target):
    """
    Find two numbers in sorted array that sum to target.
    Return their indices. arr = [1,2,3,4,6], target = 6 -> return [1,3]
    """
    # your code here
    pass

def test_two_sum_sorted():
    assert two_sum_sorted([1,2,3,4,6], 6) == [1,3]
    assert two_sum_sorted([2,7,11,15], 9) == [0,1]
    assert two_sum_sorted([1,2,3,4], 7) == [2,3]
    assert two_sum_sorted([1,2], 3) == [0,1]
''',
    },
    "sliding_window": {
        "title": "Sliding Window",
        "template": '''def max_sum_subarray(arr, k):
    """
    Find maximum sum of any contiguous subarray of size k.
    arr = [1,4,2,10,23,3,1,0,20], k = 4 -> return 39 (4+2+10+23)
    """
    # your code here
    pass

def test_max_sum_subarray():
    assert max_sum_subarray([1,4,2,10,23,3,1,0,20], 4) == 39
    assert max_sum_subarray([2,1,5,1,3,2], 3) == 9
    assert max_sum_subarray([2,3,4,1,5], 2) == 7
    assert max_sum_subarray([1], 1) == 1
''',
    },
    "tree_dfs": {
        "title": "Tree DFS",
        "template": '''class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    """
    Return inorder traversal (left, root, right).
    Tree:    2
           /   \\
          1     3
    Result: [1, 2, 3]
    """
    # your code here
    pass

def test_inorder_traversal():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert inorder_traversal(root) == [1, 2, 3]
    
    root = TreeNode(1)
    assert inorder_traversal(root) == [1]
    
    assert inorder_traversal(None) == []
''',
    },
    "recursion": {
        "title": "Recursion",
        "template": '''def factorial(n):
    """
    Calculate factorial using recursion.
    factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
    """
    # your code here - must use recursion
    pass

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(3) == 6
''',
    },
    "linked_list": {
        "title": "Linked List",
        "template": '''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a linked list and return new head.
    1->2->3 becomes 3->2->1
    """
    # your code here
    pass

def test_reverse_linked_list():
    # Create 1->2->3
    head = ListNode(1, ListNode(2, ListNode(3)))
    
    # Reverse it
    new_head = reverse_linked_list(head)
    
    # Check it's 3->2->1
    assert new_head.val == 3
    assert new_head.next.val == 2
    assert new_head.next.next.val == 1
    assert new_head.next.next.next is None
''',
    },
    "stack": {
        "title": "Stack",
        "template": '''def valid_parentheses(s):
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
''',
    },
    "dp": {
        "title": "Fibonacci with Memoization",
        "template": '''def fibonacci(n):
    """
    Calculate nth fibonacci number using memoization (DP).
    fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2)
    fibonacci(5) = 5, fibonacci(10) = 55
    """
    # your code here
    pass

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610
''',
    },
}
