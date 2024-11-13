import pytest
from min_heap_m.min_heap import sort_using_min_heap

'''  Answer

def sort_using_min_heap(arr: List[int]) -> List[int]:
    import heapq

    min_heap = []
    for x in arr:
        min_heap.append(x)
    heapq.heapify(min_heap)
    
    sorted_arr = []
    while min_heap:
        num = heapq.heappop(min_heap)
        sorted_arr.append(num)
    
    return sorted_arr

'''

def test_min_heap_with_mixed_numbers():
    assert sort_using_min_heap([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_min_heap_with_negative_numbers():
    assert sort_using_min_heap([0, -1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1, 0]

def test_min_heap_with_empty_list():
    assert sort_using_min_heap([]) == []

def test_min_heap_with_single_element():
    assert sort_using_min_heap([1]) == [1]

def test_min_heap_with_duplicate_elements():
    assert sort_using_min_heap([2, 2, 2, 2]) == [2, 2, 2, 2]

if __name__ == "__main__":
    pytest.main()