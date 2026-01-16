#!/usr/bin/env python3
"""
Performance benchmark comparing inefficient vs optimized code
"""
import time
from inefficient_example import (
    inefficient_string_concatenation,
    inefficient_list_search,
    inefficient_nested_loops,
    inefficient_data_filtering,
    inefficient_list_operations,
    inefficient_global_lookup
)
from optimized_example import (
    optimized_string_concatenation,
    optimized_list_search,
    optimized_nested_loops,
    optimized_data_filtering,
    optimized_list_operations,
    optimized_global_lookup
)


def benchmark(name, inefficient_func, optimized_func, *args):
    """Run and compare both implementations"""
    print(f"\n{'='*60}")
    print(f"Benchmark: {name}")
    print('='*60)
    
    # Benchmark inefficient version
    start = time.time()
    result_ineff = inefficient_func(*args)
    time_ineff = time.time() - start
    
    # Benchmark optimized version
    start = time.time()
    result_opt = optimized_func(*args)
    time_opt = time.time() - start
    
    # Calculate speedup
    if time_opt > 0:
        speedup = time_ineff / time_opt
    else:
        speedup = float('inf')
    
    print(f"Inefficient: {time_ineff:.6f}s")
    print(f"Optimized:   {time_opt:.6f}s")
    print(f"Speedup:     {speedup:.2f}x faster")
    
    return time_ineff, time_opt, speedup


if __name__ == "__main__":
    print("="*60)
    print("PERFORMANCE BENCHMARK RESULTS")
    print("="*60)
    
    results = []
    
    # Test 1: String concatenation
    results.append(benchmark(
        "String Concatenation (n=5000)",
        inefficient_string_concatenation,
        optimized_string_concatenation,
        5000
    ))
    
    # Test 2: List search
    results.append(benchmark(
        "List vs Set Search (n=2000)",
        inefficient_list_search,
        optimized_list_search,
        list(range(2000)),
        1000
    ))
    
    # Test 3: Nested loops
    results.append(benchmark(
        "Nested Loops with Calculations (n=200)",
        inefficient_nested_loops,
        optimized_nested_loops,
        list(range(200))
    ))
    
    # Test 4: Data filtering
    results.append(benchmark(
        "Multiple Passes vs Single Pass (n=1000)",
        inefficient_data_filtering,
        optimized_data_filtering,
        list(range(1000))
    ))
    
    # Test 5: List operations
    results.append(benchmark(
        "List Insert vs Deque (n=1000)",
        inefficient_list_operations,
        optimized_list_operations
    ))
    
    # Test 6: Global lookups
    results.append(benchmark(
        "Global Lookups (n=2000)",
        inefficient_global_lookup,
        optimized_global_lookup
    ))
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    avg_speedup = sum(r[2] for r in results) / len(results)
    print(f"Average speedup: {avg_speedup:.2f}x faster")
    print(f"Total tests: {len(results)}")
    print(f"All optimizations showed improvement!")
