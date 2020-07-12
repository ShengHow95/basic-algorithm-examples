a = [6, 3, 2, 7, 5, 5]

a = sorted(a)

for i in range(int(len(a)/2)):
    print(a[i],a[~i])