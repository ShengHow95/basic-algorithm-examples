A = [-14, -10, 2, 10, 10, 12, 12, 14, 16, 20, 30, 55, 105]

target = 10

def find_first_iterative(A, target):
    for i in range(len(A)):
        if A[i] == target:
            return i
        else:
            return None
    
def find_first_binary_search(A, target):

    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high)//2
        if A[mid] > target:
            high = mid - 1
        elif A[mid] < target:
            low = mid + 1
        elif A[mid] == target:
            if mid - 1 < 0:
                return mid
            if A[mid - 1] != target:
                return mid
            high = mid - 1

print(find_first_binary_search(A,target))
            