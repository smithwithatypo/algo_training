from typing import List

def binary_search(arr: List[int], target: int) -> int:

    # your code here
    l, r = 0, len(arr) - 1

    while l <= r: 
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1