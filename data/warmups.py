WARMUPS = {
    "binary_search": {
        "title": "Binary Search",
        "template": '''def binary_search(arr, target):
    """
    Find target in sorted array. Return index or -1 if not found.
    arr = [1,3,5,7,9], target = 5 -> return 2
    """
    # your code here
    pass

def test_binary_search():
    assert binary_search([1,3,5,7,9], 5) == 2
    assert binary_search([1,3,5,7,9], 1) == 0
    assert binary_search([1,3,5,7,9], 9) == 4
    assert binary_search([1,3,5,7,9], 4) == -1
    assert binary_search([], 1) == -1
''',
    },
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
    "count": {
        "title": "Count Using Hashmap",
        "template": '''def count_characters(s):
    """
    Count frequency of each character using a hashmap.
    "hello" -> {"h": 1, "e": 1, "l": 2, "o": 1}
    """
    # your code here
    pass

def test_count_characters():
    assert count_characters("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert count_characters("aab") == {"a": 2, "b": 1}
    assert count_characters("") == {}
    assert count_characters("a") == {"a": 1}
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
    pass

def test_valid_parentheses():
    assert valid_parentheses("()") == True
    assert valid_parentheses("()[]{}")== True
    assert valid_parentheses("(]") == False
    assert valid_parentheses("([)]") == False
    assert valid_parentheses("") == True
''',
    },
}
