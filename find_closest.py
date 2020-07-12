arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 100

def find_closest_num(arr, target):
    min_diff = float("inf")
    low = 0
    high = len(arr)-1
    closest_num = None
    
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    
    while low < high:
        mid = int((high + low)/2)

        if mid + 1 < len(arr):
            min_diff_right = abs(arr[mid+1] - target)

        if mid > 0:
            min_diff_left = abs(arr[mid-1] - target)

        if min_diff_left < min_diff_right:
            min_diff = min_diff_left
            closest_num = arr[mid-1]
        
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = arr[mid+1]
        
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return arr[mid]
    return closest_num

print(find_closest_num(arr, target))