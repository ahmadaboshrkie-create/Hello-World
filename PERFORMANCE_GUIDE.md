# Performance Optimization Guide

This repository demonstrates common performance issues in code and their optimized solutions.

## Overview

Performance optimization is crucial for creating efficient, scalable applications. This guide presents real-world examples of inefficient code patterns and their optimized alternatives.

## Python Performance Issues

### 1. String Concatenation in Loops
**Problem:** Using `+=` for strings in a loop creates a new string object each time (O(n²) complexity)
```python
# Inefficient
result = ""
for i in range(n):
    result += str(i) + ","
```
**Solution:** Use `join()` with a list or generator (O(n) complexity)
```python
# Optimized
result = ",".join(str(i) for i in range(n))
```
**Performance Impact:** 10-100x faster for large datasets

### 2. Membership Testing with Lists
**Problem:** Using `in` operator on lists requires O(n) search time
```python
# Inefficient
found_items = []
if item in found_items:  # O(n) lookup
    ...
```
**Solution:** Use sets for O(1) membership testing
```python
# Optimized
found_items = set()
if item in found_items:  # O(1) lookup
    ...
```
**Performance Impact:** Significant improvement for large datasets

### 3. Repeated Calculations in Loops
**Problem:** Computing the same value multiple times wastes CPU cycles
```python
# Inefficient
for i in range(len(data)):
    for j in range(len(data)):
        value = data[i] * 2 + data[j] * 2  # Repeated multiplication
```
**Solution:** Calculate once and reuse
```python
# Optimized
doubled_data = [x * 2 for x in data]
result = [doubled_data[i] + doubled_data[j] for i in range(len(data)) for j in range(len(data))]
```

### 4. File I/O Operations
**Problem:** Opening/closing files repeatedly incurs significant overhead
```python
# Inefficient
for i in range(100):
    with open('file.txt', 'a') as f:
        f.write(f"Line {i}\n")
```
**Solution:** Batch operations and keep file open
```python
# Optimized
with open('file.txt', 'a') as f:
    f.writelines(f"Line {i}\n" for i in range(100))
```
**Performance Impact:** 50-100x faster

### 5. Multiple Passes Over Data
**Problem:** Iterating over data multiple times when one pass would suffice
```python
# Inefficient - 3 passes
evens = [num for num in numbers if num % 2 == 0]
large_evens = [num for num in evens if num > 10]
result = [num ** 2 for num in large_evens]
```
**Solution:** Combine filters in single pass
```python
# Optimized - 1 pass
result = [num ** 2 for num in numbers if num % 2 == 0 and num > 10]
```

### 6. List Operations at Beginning
**Problem:** `insert(0, x)` is O(n) as it shifts all elements
```python
# Inefficient
result = []
for i in range(1000):
    result.insert(0, i)  # O(n) each time = O(n²) total
```
**Solution:** Use `collections.deque` or reverse after building
```python
# Optimized
from collections import deque
result = deque()
for i in range(1000):
    result.appendleft(i)  # O(1)
```

### 7. Global Variable Lookups
**Problem:** Global lookups are slower than local variable access
```python
# Inefficient
for i in range(1000):
    result.append(len(str(i)))  # Global lookup each time
```
**Solution:** Cache globals in local scope
```python
# Optimized
str_func = str
len_func = len
for i in range(1000):
    result.append(len_func(str_func(i)))
```

## Shell Script Performance Issues

### 1. Repeated Command Execution
**Problem:** Calling external commands in loops is expensive (process creation overhead)
```bash
# Inefficient
for i in {1..100}; do
    date >> /tmp/dates.txt
done
```
**Solution:** Cache command output and reuse
```bash
# Optimized
date_output=$(date)
for i in {1..100}; do
    echo "$date_output" >> /tmp/dates.txt
done
```

### 2. Useless Use of Cat (UUOC)
**Problem:** Spawning unnecessary processes
```bash
# Inefficient
cat file.txt | grep "pattern"
```
**Solution:** Use redirection directly
```bash
# Optimized
grep "pattern" < file.txt
```

### 3. External Commands vs Built-ins
**Problem:** External commands like `basename` require process creation
```bash
# Inefficient
basename "$file"
```
**Solution:** Use bash parameter expansion
```bash
# Optimized
echo "${file##*/}"
```

### 4. Subshells in Loops
**Problem:** Command substitution in loops creates subshells
```bash
# Inefficient
for i in $(seq 1 20); do
    result=$(echo "$i * 2" | bc)
done
```
**Solution:** Use bash arithmetic
```bash
# Optimized
for ((i=1; i<=20; i++)); do
    result=$((i * 2))
done
```

### 5. Multiple File Reads
**Problem:** Reading the same file multiple times
```bash
# Inefficient
grep "Jan" file.txt > jan.txt
grep "Feb" file.txt > feb.txt
grep "Mar" file.txt > mar.txt
```
**Solution:** Single pass with awk
```bash
# Optimized
awk '/Jan/ {print > "jan.txt"} /Feb/ {print > "feb.txt"} /Mar/ {print > "mar.txt"}' file.txt
```

### 6. Parsing ls Output
**Problem:** Using `ls` in scripts can break with special characters
```bash
# Inefficient
files=$(ls /tmp/*.txt)
for file in $files; do
    echo "$file"
done
```
**Solution:** Use glob patterns directly
```bash
# Optimized
files=(/tmp/*.txt)
for file in "${files[@]}"; do
    echo "$file"
done
```

## Performance Testing

To compare performance:

1. **Python Examples:**
```bash
python3 inefficient_example.py
python3 optimized_example.py
```

2. **Shell Script Examples:**
```bash
chmod +x inefficient_script.sh optimized_script.sh
time ./inefficient_script.sh
time ./optimized_script.sh
```

## Key Takeaways

1. **Choose the right data structure:** Sets for membership testing, deques for double-ended operations
2. **Minimize I/O operations:** Batch reads/writes, keep files open when needed
3. **Avoid repeated work:** Cache calculations, use single-pass algorithms
4. **Use built-in functions:** They're optimized and faster than external tools
5. **Understand complexity:** Know the Big O of your operations
6. **Profile before optimizing:** Measure to find real bottlenecks

## Complexity Cheat Sheet

| Operation | List | Set | Dict |
|-----------|------|-----|------|
| Access by index | O(1) | N/A | N/A |
| Search | O(n) | O(1) | O(1) |
| Insert at end | O(1) | O(1) | O(1) |
| Insert at beginning | O(n) | O(1) | O(1) |
| Delete | O(n) | O(1) | O(1) |

## Further Resources

- Python Performance Tips: https://wiki.python.org/moin/PythonSpeed/PerformanceTips
- Bash Best Practices: https://google.github.io/styleguide/shellguide.html
- Big O Notation Guide: https://www.bigocheatsheet.com/
