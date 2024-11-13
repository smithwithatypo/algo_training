def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return "Invalid"
    
    # Compute the sum of the first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window from start to end in the array
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(max_sum_subarray(arr, k))  # Output: 27 


'''
probably should separate these into two separate directories/modules






'''

def smallest_subarray_with_given_sum(arr, S):
    n = len(arr)
    min_length = float('inf')
    window_sum = 0
    left = 0

    for right in range(n):
        window_sum += arr[right]

        while window_sum >= S:
            min_length = min(min_length, right - left + 1)
            window_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0

# Example usage
arr = [2, 1, 5, 2, 3, 2]
S = 7
print(smallest_subarray_with_given_sum(arr, S))  # Output: 2