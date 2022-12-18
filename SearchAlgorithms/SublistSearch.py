# Sublist Search Algorithm

def sublist_search(arr, subarr):
    for i in range(len(arr)):
        if arr[i] == subarr[0]:
            for j in range(len(subarr)):
                if arr[i + j] != subarr[j]:
                    break
                if j == len(subarr) - 1:
                    return i
    return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    subarr = [10, 40]
    result = sublist_search(arr, subarr)
    if result == -1:
        print("Sublist not found in the array")
    else:
        print("Sublist found at index", result)



