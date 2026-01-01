# Rep 3/3 - Count Using Hashmap


def count_characters(s):
    """
    Count frequency of each character using a hashmap.
    "hello" -> {"h": 1, "e": 1, "l": 2, "o": 1}
    """
    # your code here
    from collections import Counter
    return Counter(s)
    pass

def test_count_characters():
    assert count_characters("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert count_characters("aab") == {"a": 2, "b": 1}
    assert count_characters("") == {}
    assert count_characters("a") == {"a": 1}
