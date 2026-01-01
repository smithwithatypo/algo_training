WARMUPS = {
    "contains_duplicate": {
        "title": "Contains Duplicate",
        "template": '''def contains_duplicate(nums):
    """
    Return True if any value appears at least twice in the array.
    nums = [1, 2, 3, 1] -> True
    nums = [1, 2, 3, 4] -> False
    """
    # your code here
    pass

def test_contains_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) == True
    assert contains_duplicate([1, 2, 3, 4]) == False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    assert contains_duplicate([]) == False
    assert contains_duplicate([1]) == False
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
    "valid_anagram": {
        "title": "Valid Anagram",
        "template": '''def valid_anagram(s, t):
    """
    Check if t is an anagram of s (same letters, different order).
    s = "anagram", t = "nagaram" -> True
    s = "rat", t = "car" -> False
    """
    # your code here
    pass

def test_valid_anagram():
    assert valid_anagram("anagram", "nagaram") == True
    assert valid_anagram("rat", "car") == False
    assert valid_anagram("", "") == True
    assert valid_anagram("a", "a") == True
    assert valid_anagram("ab", "ba") == True
''',
    },
    "prefix_sum": {
        "title": "Prefix Sum",
        "template": '''def prefix_sum(arr):
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
''',
    },
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
}
