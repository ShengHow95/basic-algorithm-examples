str_permutation1 = "dog"
str_permutation2 = "god"

not_str_permutation1 = "not"
not_str_permutation2 = "no"

def is_perm_str_ht(str1, str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()

    ht = dict()

    if len(str1) != len(str2):
        return False

    for i in str1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    
    for i in str2:
        if i in ht:
            ht[i] -= 1
        else:
            return False
    else:
        return True

def is_perm_str_sort(str1, str2):
    str1 = sorted(str1.replace(" ","").lower())
    str2 = sorted(str2.replace(" ","").lower())

    if str1 != str2:
        return False
    else:
        return True

print(is_perm_str_ht(str_permutation1,str_permutation2))
print(is_perm_str_ht(not_str_permutation1,not_str_permutation2))
print(is_perm_str_sort(str_permutation1,str_permutation2))
print(is_perm_str_sort(not_str_permutation1,not_str_permutation2))
