x = 500
y = 3000

def recursive_multiply(x, y):
    if(x < y):
        x , y = y , x
    if y == 0:
        return 0
    return x + recursive_multiply(x, y-1)

print(recursive_multiply(x,y))