data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
target = 9

# Iterative Binary Search
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = int((low + high)/2)
        if target == data[mid]:
            return "Target Exists"
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return "Target NOT Exists!"

# Recursive Binary Search
def binary_search_recursive(data, target, low, high):
    if low > high:
        return "Target NOT Exists!"
    else:
        mid = int((low + high)/2)
        if target == data[mid]:
            return "Target Exists"
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else:
            return binary_search_recursive(data, target, mid+1, high)

print(binary_search_iterative(data, target))
print(binary_search_recursive(data, target, 0, len(data)-1))