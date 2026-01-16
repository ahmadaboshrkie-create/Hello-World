#!/bin/bash
# Optimized version of the shell script with performance improvements

echo "=== Optimized Shell Script Examples ==="

# Optimization 1: Batch command execution
# Cache results instead of calling repeatedly
echo "Example 1: Cached command execution"
date_output=$(date)
user_output=$(whoami)
host_output=$(hostname)
for i in {1..100}; do
    echo "$date_output" >> /tmp/dates_opt.txt
    echo "$user_output" >> /tmp/users_opt.txt
    echo "$host_output" >> /tmp/hosts_opt.txt
done

# Optimization 2: Use redirection directly
# Avoid spawning extra cat process
echo "Example 2: Direct redirection"
grep "2026" < /tmp/dates_opt.txt > /tmp/filtered_opt.txt

# Optimization 3: Use arrays for efficient concatenation
# Build array then join once
echo "Example 3: Array-based string building"
numbers=()
for i in {1..50}; do
    numbers+=("$i")
done
printf "%s," "${numbers[@]}" > /tmp/numbers_opt.txt

# Optimization 4: Use bash built-ins
# Avoid external command overhead
echo "Example 4: Built-in parameter expansion"
for file in /tmp/*.txt; do
    if [ -f "$file" ]; then
        echo "${file##*/}"  # bash built-in parameter expansion
    fi
done

# Optimization 5: Efficient file reading without subshell
# Use proper redirection to avoid subshell
echo "Example 5: Efficient file reading"
while read -r line; do
    echo "Processing: $line"
done < /tmp/dates_opt.txt > /tmp/processed_opt.txt

# Optimization 6: Single pass with awk or single grep with multiple patterns
# Read file once instead of three times
echo "Example 6: Single pass filtering"
awk '/Jan/ {print > "/tmp/jan_opt.txt"} 
     /Feb/ {print > "/tmp/feb_opt.txt"} 
     /Mar/ {print > "/tmp/mar_opt.txt"}' /tmp/dates_opt.txt

# Optimization 7: Use arrays properly
# Glob directly into array instead of ls
echo "Example 7: Proper array usage"
files=(/tmp/*.txt)
for file in "${files[@]}"; do
    echo "File: $file"
done

# Optimization 8: Use bash arithmetic instead of bc
# Built-in arithmetic is much faster
echo "Example 8: Built-in arithmetic"
for ((i=1; i<=20; i++)); do
    result=$((i * 2))
    echo "$result"
done > /tmp/calculations_opt.txt

echo "Optimized script completed"
