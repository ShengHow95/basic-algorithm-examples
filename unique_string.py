unique_str = "AbcdEfg"
non_unique_str = "Abcsdwd"

def is_unique_ht(str1):
    str1 = str1.replace(" ", "").lower()

    ht = dict()

    for i in str1:
        if i in ht:
            return False
        else:
            ht[i] = 1
    else:
        return True

def is_unique_set(str1):
    str1 = str1.replace(" ", "").lower()
    return len(set(str1)) == len(str1)

def is_unique_iterative(str1):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    str1 = str1.replace(" ", "").lower()

    for i in str1:
        if i in alpha:
            alpha = alpha.replace(i,"")
        else:
            return False
    else:
        return True

print(is_unique_ht(unique_str))
print(is_unique_ht(non_unique_str))
print(is_unique_set(unique_str))
print(is_unique_set(non_unique_str))
print(is_unique_iterative(unique_str))
print(is_unique_iterative(non_unique_str))