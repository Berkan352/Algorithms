# Fibonacci Search Algorithm

def fibonacci_search(arr, x):
    n = len(arr)
    fib2 = 0
    fib1 = 1
    fib = fib2 + fib1
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
    offset = -1
    while fib > 1:
        i = min(offset + fib2, n - 1)
        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    return offset + 1 if fib1 and arr[offset + 1] == x else -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = fibonacci_search(arr, x)
    if result == -1:
        print("Element not found in the array")
    else:
        print("Element found at index", result)