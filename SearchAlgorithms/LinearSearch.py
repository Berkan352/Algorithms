# Sequential Search

def linear_search(arr, x):
    return next((i for i in range(len(arr)) if arr[i] == x), -1)


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = linear_search(arr, x)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)





