# warmup_solutions.py


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []


def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum


def count_characters(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    return counts


def inorder_traversal(root):
    result = []

    def helper(node):
        if node:
            helper(node.left)
            result.append(node.val)
            helper(node.right)

    helper(root)
    return result


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def valid_parentheses(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0


def prefix_sum(arr):
    if not arr:
        return []
    result = [arr[0]]
    for i in range(1, len(arr)):
        result.append(result[i - 1] + arr[i])
    return result


def fibonacci(n):
    memo = {}

    def helper(n):
        if n <= 1:
            return n
        if n in memo:
            return memo[n]
        memo[n] = helper(n - 1) + helper(n - 2)
        return memo[n]

    return helper(n)


def contains_duplicate(nums):
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False
