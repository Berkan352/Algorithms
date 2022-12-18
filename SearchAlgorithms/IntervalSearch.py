# Interval Search


def interval_search(arr, x):
    n = len(arr)
    if x < arr[0] or x > arr[n - 1]:
        return -1
    i = 0
    j = n - 1
    while i <= j and x >= arr[i] and x <= arr[j]:
        if i == j:
            return i if arr[i] == x else -1
        pos = i + int(((float(j - i) / (arr[j] - arr[i])) * (x - arr[i])))
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            i = pos + 1
        else:
            j = pos - 1
    return -1


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = interval_search(arr, x)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)

