#!/usr/bin/env python3
"""
Example of inefficient Python code with common performance issues
"""
import time


def inefficient_string_concatenation(n):
    """
    Issue: Using + for string concatenation in a loop
    O(n^2) complexity due to string immutability
    """
    result = ""
    for i in range(n):
        result += str(i) + ","
    return result


def inefficient_list_search(items, target):
    """
    Issue: Using list for membership testing
    O(n) lookup time for each check
    """
    found_items = []
    for item in items:
        if item in found_items:
            continue
        if item == target:
            found_items.append(item)
    return found_items


def inefficient_nested_loops(data):
    """
    Issue: Nested loops with repeated calculations
    Unnecessary O(n^2) operations
    """
    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            # Repeated calculation in inner loop
            value = data[i] * 2 + data[j] * 2
            result.append(value)
    return result


def inefficient_file_operations():
    """
    Issue: Opening/closing file multiple times
    Expensive I/O operations repeated unnecessarily
    """
    for i in range(100):
        with open('/tmp/test.txt', 'a') as f:
            f.write(f"Line {i}\n")


def inefficient_dictionary_access(data_dict):
    """
    Issue: Repeated dictionary key checks
    Multiple lookups for the same key
    """
    result = []
    for key in data_dict:
        if key in data_dict:
            if key in data_dict:
                result.append(data_dict[key])
    return result


def inefficient_list_operations():
    """
    Issue: Using list methods inefficiently
    insert(0, x) is O(n), repeated calls make it O(n^2)
    """
    result = []
    for i in range(1000):
        result.insert(0, i)  # Always inserting at beginning
    return result


def inefficient_data_filtering(numbers):
    """
    Issue: Multiple passes over the same data
    Could be done in a single pass
    """
    # First pass: filter evens
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    
    # Second pass: filter > 10
    large_evens = []
    for num in evens:
        if num > 10:
            large_evens.append(num)
    
    # Third pass: square them
    result = []
    for num in large_evens:
        result.append(num ** 2)
    
    return result


def inefficient_global_lookup():
    """
    Issue: Repeated global lookups in loop
    Each lookup has overhead
    """
    result = []
    for i in range(1000):
        result.append(len(str(i)))
    return result


if __name__ == "__main__":
    print("Running inefficient code examples...")
    
    # Test string concatenation
    start = time.time()
    inefficient_string_concatenation(1000)
    print(f"String concatenation: {time.time() - start:.4f}s")
    
    # Test list search
    start = time.time()
    items = list(range(1000))
    inefficient_list_search(items, 500)
    print(f"List search: {time.time() - start:.4f}s")
    
    # Test nested loops
    start = time.time()
    inefficient_nested_loops(list(range(100)))
    print(f"Nested loops: {time.time() - start:.4f}s")
    
    # Test data filtering
    start = time.time()
    inefficient_data_filtering(list(range(100)))
    print(f"Data filtering: {time.time() - start:.4f}s")
