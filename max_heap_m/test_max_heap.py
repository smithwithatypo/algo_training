import pytest
from max_heap_m.max_heap import sort_using_max_heap

'''  Answer

def sort_using_max_heap(arr: List[int]) -> List[int]:
    import heapq

    max_heap = []
    for x in arr:
        max_heap.append(-x)
    heapq.heapify(max_heap)
    
    sorted_arr = []
    while max_heap:
        num = -heapq.heappop(max_heap)
        sorted_arr.append(num)
    
    return sorted_arr


'''

def test_max_heap_with_mixed_numbers():
    assert sort_using_max_heap([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

def test_max_heap_with_negative_numbers():
    assert sort_using_max_heap([0, -1, -2, -3, -4, -5]) == [0, -1, -2, -3, -4, -5]

def test_max_heap_with_empty_list():
    assert sort_using_max_heap([]) == []

def test_max_heap_with_single_element():
    assert sort_using_max_heap([1]) == [1]

def test_max_heap_with_duplicate_elements():
    assert sort_using_max_heap([2, 2, 2, 2]) == [2, 2, 2, 2]

if __name__ == "__main__":
    pytest.main()