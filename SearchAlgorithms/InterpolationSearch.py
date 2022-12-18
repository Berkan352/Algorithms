# Interpolation Search Algorithm

def interpolation_search(arr, x):
    lo = 0
    hi = (len(arr) - 1)

    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        if lo == hi:
            return lo if arr[lo] == x else -1
        pos = lo + int(((float(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo])))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            lo = pos + 1
        else:
            hi = pos - 1

    return -1


if __name__ == '__main__':
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    x = 18
    index = interpolation_search(arr, x)

    if index != -1:
        print("Element found at index", index)
    else:
        print("Element not found")