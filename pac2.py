import time
import random

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


n = int(input("Enter size of array: "))
arr = sorted(random.sample(range(1, n * 10), n))

target = int(input("Enter element to search: "))

start_time = time.time()
index_linear = linear_search(arr, target)
end_time = time.time()
linear_time = (end_time - start_time) * 1e6  

start_time = time.time()
index_binary = binary_search(arr, target)
end_time = time.time()
binary_time = (end_time - start_time) * 1e6  
print("\nArray Size:", n)
print("Target Element:", target)
print("Linear Search: Index =", index_linear, " Time =", linear_time, "microseconds")
print("Binary Search: Index =", index_binary, " Time =", binary_time, "microseconds")
