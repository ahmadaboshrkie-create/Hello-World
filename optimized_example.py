#!/usr/bin/env python3
"""
Optimized versions of the inefficient code examples
"""
from collections import deque
import time


def optimized_string_concatenation(n):
    """
    Optimization: Use list and join()
    O(n) complexity - much faster for large n
    """
    return ",".join(str(i) for i in range(n))


def optimized_list_search(items, target):
    """
    Optimization: Use set for O(1) membership testing
    Significant speedup for large datasets
    """
    found_items = set()
    result = []
    for item in items:
        if item in found_items:
            continue
        found_items.add(item)
        if item == target:
            result.append(item)
    return result


def optimized_nested_loops(data):
    """
    Optimization: Calculate once, use list comprehension
    Reduce redundant calculations and improve readability
    """
    doubled_data = [x * 2 for x in data]
    result = [doubled_data[i] + doubled_data[j] 
              for i in range(len(data)) 
              for j in range(len(data))]
    return result


def optimized_file_operations():
    """
    Optimization: Open file once and batch write
    Significantly reduces I/O overhead
    """
    with open('/tmp/test.txt', 'a') as f:
        f.writelines(f"Line {i}\n" for i in range(100))


def optimized_dictionary_access(data_dict):
    """
    Optimization: Iterate over items() directly
    Single lookup instead of multiple - when iterating keys that exist in dict,
    the checks are redundant so we can just access values directly
    """
    result = []
    for key in data_dict:
        result.append(data_dict[key])
    return result


def optimized_list_operations():
    """
    Optimization: Use deque or reverse the list once
    appendleft() on deque is O(1), or build list and reverse once
    """
    result = deque()
    for i in range(1000):
        result.appendleft(i)
    return list(result)


def optimized_data_filtering(numbers):
    """
    Optimization: Single pass with generator expression or list comprehension
    Process all conditions in one iteration
    """
    return [num ** 2 for num in numbers if num % 2 == 0 and num > 10]


def optimized_global_lookup():
    """
    Optimization: Cache global references in local scope
    Local variable access is faster than global
    """
    result = []
    str_func = str
    len_func = len
    for i in range(1000):
        result.append(len_func(str_func(i)))
    return result


if __name__ == "__main__":
    print("Running optimized code examples...")
    
    # Test string concatenation
    start = time.time()
    optimized_string_concatenation(1000)
    print(f"String concatenation: {time.time() - start:.4f}s")
    
    # Test list search
    start = time.time()
    items = list(range(1000))
    optimized_list_search(items, 500)
    print(f"List search: {time.time() - start:.4f}s")
    
    # Test nested loops
    start = time.time()
    optimized_nested_loops(list(range(100)))
    print(f"Nested loops: {time.time() - start:.4f}s")
    
    # Test data filtering
    start = time.time()
    optimized_data_filtering(list(range(100)))
    print(f"Data filtering: {time.time() - start:.4f}s")
