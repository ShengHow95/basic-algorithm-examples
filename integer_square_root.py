def integer_square_root(num):
    low = 0
    high = num

    while low <= high:
        print(low, high)
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= num:
            low = mid + 1
        else:
            high = mid - 1
    else:
        return low - 1

print(integer_square_root(9))