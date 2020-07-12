A = [1, 6, 3, 2, 1]

def find_highest(A):
    low = 0
    high = len(A) - 1

    if len(A) < 3:
        return None

    while low < high:
        mid = (low + high)//2

        print(mid, A[mid])

        if (A[mid] < A[mid-1] and A[mid-1] > 0):
            high = mid - 1
        elif (A[mid] < A[mid+1] and A[mid+1] < len(A)):
            low = mid + 1
        elif (A[mid] > A[mid-1] and A[mid] > A[mid+1]):
            return A[mid]
    else:
        return None

print(max(A))
print(find_highest(A))