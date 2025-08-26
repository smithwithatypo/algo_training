# Rep 1/1 - OOP Basics


class Counter:
    """
    Simple counter that can increment, decrement, and get value.
    """
    def __init__(self):
        # your code here
        return "yo"
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
