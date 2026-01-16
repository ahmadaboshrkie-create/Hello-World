#!/bin/bash
# Example of inefficient shell script with common performance issues

echo "=== Inefficient Shell Script Examples ==="

# Issue 1: Repeated command execution in loop
# Problem: Calling external commands repeatedly is expensive
echo "Example 1: Repeated command execution"
for i in {1..100}; do
    date >> /tmp/dates.txt
    whoami >> /tmp/users.txt
    hostname >> /tmp/hosts.txt
done

# Issue 2: Using cat unnecessarily (useless use of cat)
# Problem: Spawning extra process when redirection would work
echo "Example 2: Useless use of cat"
cat /tmp/dates.txt | grep "2026" > /tmp/filtered.txt

# Issue 3: Inefficient string concatenation in loop
# Problem: Creating subshells and command substitution repeatedly
echo "Example 3: Inefficient string building"
result=""
for i in {1..50}; do
    result="${result}${i},"
done
echo "$result" > /tmp/numbers.txt

# Issue 4: Not using built-in commands
# Problem: External command overhead when bash built-ins are available
echo "Example 4: External commands instead of built-ins"
for file in /tmp/*.txt; do
    if [ -f "$file" ]; then
        basename "$file"
    fi
done

# Issue 5: Reading files line by line inefficiently
# Problem: Subshell in while loop, slow processing
echo "Example 5: Inefficient file reading"
cat /tmp/dates.txt | while read line; do
    echo "Processing: $line"
done > /tmp/processed.txt

# Issue 6: Repeated grep on same file
# Problem: Reading file multiple times instead of once
echo "Example 6: Multiple passes over same file"
grep "Jan" /tmp/dates.txt > /tmp/jan.txt
grep "Feb" /tmp/dates.txt > /tmp/feb.txt
grep "Mar" /tmp/dates.txt > /tmp/mar.txt

# Issue 7: Not using arrays efficiently
# Problem: String manipulation when arrays would be better
echo "Example 7: Inefficient list handling"
files=$(ls /tmp/*.txt)
for file in $files; do
    echo "File: $file"
done

# Issue 8: Spawning subshells unnecessarily
# Problem: Using command substitution when not needed
echo "Example 8: Unnecessary subshells"
for i in $(seq 1 20); do
    result=$(echo "$i * 2" | bc)
    echo "$result"
done > /tmp/calculations.txt

echo "Inefficient script completed"
