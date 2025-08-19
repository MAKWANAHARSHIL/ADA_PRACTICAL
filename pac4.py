import time

def fact_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * fact_recursive(n - 1)

def fact_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a number: "))

start = time.time()
rec = fact_recursive(n)
end = time.time()
print("\nRecursive Factorial:", rec)
print("Time (Recursive):", end - start, "seconds")

start = time.time()
ite = fact_iterative(n)
end = time.time()
print("\nIterative Factorial:", ite)
print("Time (Iterative):", end - start, "seconds")
