# problems.py

PROBLEMS = {
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
'''
    },

    "oop_basics": {
        "title": "OOP Basics",
        "template": '''class Counter:
    """
    Simple counter that can increment, decrement, and get value.
    """
    def __init__(self):
        # your code here
        pass
    
    def increment(self):
        # your code here
        pass
    
    def decrement(self):
        # your code here
        pass
    
    def get_value(self):
        # your code here
        pass

def test_counter():
    c = Counter()
    assert c.get_value() == 0
    c.increment()
    assert c.get_value() == 1
    c.increment()
    assert c.get_value() == 2
    c.decrement()
    assert c.get_value() == 1
'''
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
'''
    },

    "min_heap": {
        "title": "Min Heap",
        "template": '''import heapq

def find_k_smallest(nums, k):
    """
    Find the k smallest elements using a min heap.
    nums = [3,1,5,12,2,11], k = 3 -> return [1,2,3]
    """
    # your code here
    pass

def test_find_k_smallest():
    assert find_k_smallest([3,1,5,12,2,11], 3) == [1,2,3]
    assert find_k_smallest([1,2,3,4,5], 2) == [1,2]
    assert find_k_smallest([5], 1) == [5]
    assert find_k_smallest([3,2,1], 3) == [1,2,3]
'''
    },

    "max_heap": {
        "title": "Max Heap",
        "template": '''import heapq

def find_k_largest(nums, k):
    """
    Find the k largest elements using a max heap.
    nums = [3,1,5,12,2,11], k = 3 -> return [12,11,5]
    """
    # your code here
    pass

def test_find_k_largest():
    assert find_k_largest([3,1,5,12,2,11], 3) == [12,11,5]
    assert find_k_largest([1,2,3,4,5], 2) == [5,4]
    assert find_k_largest([5], 1) == [5]
    assert find_k_largest([3,2,1], 3) == [3,2,1]
'''
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
'''
    },

    "sort_inplace_vs_copy": {
        "title": "Sort In-Place vs Copy",
        "template": '''def sort_both_ways(arr):
    """
    Return tuple: (original_array_sorted_inplace, new_sorted_array)
    Original array should be modified, new array should be separate.
    """
    # your code here
    pass

def test_sort_both_ways():
    arr1 = [3,1,4,1,5]
    result = sort_both_ways(arr1)
    assert arr1 == [1,1,3,4,5]  # original modified
    assert result[0] == [1,1,3,4,5]  # return inplace result
    assert result[1] == [1,1,3,4,5]  # return copy result
    assert result[0] is arr1  # should be same object
    assert result[1] is not arr1  # should be different object
'''
    },

    "count_using_hashmap": {
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
'''
    },

    "count_alphabet_bucket_sort": {
        "title": "Count Alphabet Using Bucket Sort",
        "template": '''def count_letters(s):
    """
    Count only lowercase letters a-z using fixed-size array (bucket sort concept).
    Return list of 26 counts. "abc" -> [1,1,1,0,0,...,0]
    """
    # your code here
    pass

def test_count_letters():
    result = count_letters("abc")
    assert result[:3] == [1,1,1]
    assert sum(result[3:]) == 0
    assert len(result) == 26
    
    result = count_letters("hello")
    assert result[4] == 1  # e
    assert result[7] == 1  # h
    assert result[11] == 2  # l
    assert result[14] == 1  # o
'''
    },

    "list_comprehension": {
        "title": "List Comprehension",
        "template": '''def process_numbers(nums):
    """
    Return list of squares of even numbers only, using list comprehension.
    [1,2,3,4,5,6] -> [4,16,36]
    """
    # your code here - must use list comprehension
    pass

def test_process_numbers():
    assert process_numbers([1,2,3,4,5,6]) == [4,16,36]
    assert process_numbers([1,3,5]) == []
    assert process_numbers([2,4]) == [4,16]
    assert process_numbers([]) == []
'''
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
'''
    },

    "quick_sort": {
        "title": "Quick Sort",
        "template": '''def quick_sort(arr):
    """
    Sort array using quicksort algorithm.
    [3,1,4,1,5] -> [1,1,3,4,5]
    """
    # your code here
    pass

def test_quick_sort():
    assert quick_sort([3,1,4,1,5]) == [1,1,3,4,5]
    assert quick_sort([1]) == [1]
    assert quick_sort([]) == []
    assert quick_sort([3,2,1]) == [1,2,3]
'''
    },

    "merge_sort": {
        "title": "Merge Sort",
        "template": '''def merge_sort(arr):
    """
    Sort array using merge sort algorithm.
    [3,1,4,1,5] -> [1,1,3,4,5]
    """
    # your code here
    pass

def test_merge_sort():
    assert merge_sort([3,1,4,1,5]) == [1,1,3,4,5]
    assert merge_sort([1]) == [1]
    assert merge_sort([]) == []
    assert merge_sort([3,2,1]) == [1,2,3]
'''
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
'''
    },

    "tree_bfs": {
        "title": "Tree BFS",
        "template": '''from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    """
    Return list of values in level-order (BFS).
    Tree:    1
           /   \\
          2     3
    Result: [1, 2, 3]
    """
    # your code here
    pass

def test_level_order_traversal():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert level_order_traversal(root) == [1, 2, 3]
    
    root = TreeNode(1)
    assert level_order_traversal(root) == [1]
    
    assert level_order_traversal(None) == []
'''
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
'''
    },

    "graph_bfs": {
        "title": "Graph BFS",
        "template": '''from collections import deque

def bfs_shortest_path(graph, start, end):
    """
    Find shortest path length using BFS.
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    start = "A", end = "D" -> return 2
    """
    # your code here
    pass

def test_bfs_shortest_path():
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    assert bfs_shortest_path(graph, "A", "D") == 2
    assert bfs_shortest_path(graph, "A", "A") == 0
    
    graph2 = {"A": ["B"], "B": []}
    assert bfs_shortest_path(graph2, "A", "B") == 1
'''
    },

    "graph_dfs": {
        "title": "Graph DFS",
        "template": '''def has_path_dfs(graph, start, end):
    """
    Check if path exists from start to end using DFS.
    graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
    start = "A", end = "D" -> return True
    """
    # your code here
    pass

def test_has_path_dfs():
    graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
    assert has_path_dfs(graph, "A", "D") == True
    assert has_path_dfs(graph, "A", "A") == True
    assert has_path_dfs(graph, "C", "D") == False
'''
    },

    "dfs_directions": {
        "title": "DFS: Directions for Graph Traversal",
        "template": '''def count_islands(grid):
    """
    Count islands in 2D grid using DFS with 4-directional movement.
    grid = [["1","1","0"],["1","0","0"],["0","0","1"]] -> return 2
    """
    # your code here - define directions and use DFS
    pass

def test_count_islands():
    grid1 = [["1","1","0"],["1","0","0"],["0","0","1"]]
    assert count_islands(grid1) == 2
    
    grid2 = [["1","1","1"],["0","1","0"],["1","1","1"]]
    assert count_islands(grid2) == 1
    
    assert count_islands([]) == 0
'''
    },

    "dfs_base_cases": {
        "title": "DFS: Base Cases for Graph Traversal",
        "template": '''def max_path_sum(grid):
    """
    Find maximum path sum from top-left to bottom-right.
    Only move right or down. Use DFS with proper base cases.
    grid = [[1,3,1],[1,5,1],[4,2,1]] -> return 12 (1+3+5+2+1)
    """
    # your code here - focus on base cases
    pass

def test_max_path_sum():
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    assert max_path_sum(grid) == 12
    
    assert max_path_sum([[1]]) == 1
    assert max_path_sum([[1,2],[3,4]]) == 8
'''
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
'''
    },

    "prefix_sum": {
        "title": "Prefix Sum",
        "template": '''def range_sum_query(nums, queries):
    """
    Answer multiple range sum queries efficiently using prefix sum.
    nums = [1,2,3,4], queries = [(0,2), (1,3)] -> return [6, 9]
    """
    # your code here
    pass

def test_range_sum_query():
    assert range_sum_query([1,2,3,4], [(0,2), (1,3)]) == [6, 9]
    assert range_sum_query([1], [(0,0)]) == [1]
    assert range_sum_query([1,2,3], [(0,2), (0,1)]) == [6, 3]
'''
    },

    "queue": {
        "title": "Queue",
        "template": '''from collections import deque

def sliding_window_maximum(nums, k):
    """
    Find maximum in each sliding window of size k using a deque.
    nums = [1,3,-1,-3,5,3,6,7], k = 3 -> return [3,3,5,5,6,7]
    """
    # your code here
    pass

def test_sliding_window_maximum():
    assert sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert sliding_window_maximum([1], 1) == [1]
    assert sliding_window_maximum([1,2,3], 2) == [2,3]
'''
    },

    "greedy": {
        "title": "Greedy",
        "template": '''def max_meetings(start_times, end_times):
    """
    Select maximum number of non-overlapping meetings using greedy approach.
    start = [1,3,0,5,8,5], end = [2,4,6,7,9,9] -> return 4
    """
    # your code here
    pass

def test_max_meetings():
    start = [1,3,0,5,8,5]
    end = [2,4,6,7,9,9]
    assert max_meetings(start, end) == 4
    
    assert max_meetings([1], [2]) == 1
    assert max_meetings([1,2], [2,3]) == 2
'''
    },

    "dynamic_programming": {
        "title": "Dynamic Programming",
        "template": '''def climb_stairs(n):
    """
    Count ways to climb n stairs (1 or 2 steps at a time) using DP.
    n = 3 -> return 3 (1+1+1, 1+2, 2+1)
    """
    # your code here
    pass

def test_climb_stairs():
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5
    assert climb_stairs(5) == 8
'''
    }
}