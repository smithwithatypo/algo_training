# Rep 2/2 - OOP Basics
# ⚠ Failed test(s) last time


class Counter:
    """
    Simple counter that can increment, decrement, and get value.
    """
    def __init__(self):
        # your code here
        self.value = 0
        pass
    
    def increment(self):
        # your code here
        self.value += 2
        pass
    
    def decrement(self):
        # your code here
        self.value -= 10
        pass
    
    def get_value(self):
        # your code here
        return self.value
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
