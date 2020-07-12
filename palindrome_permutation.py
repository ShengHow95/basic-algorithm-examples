palin_perm = "Tact Coa"
not_palin_perm = "This is not palindrome permutation"

def is_panlindrome_permutation(s):
    s = s.replace(" ", "").lower()
    ht = dict()

    for i in s:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    
    odd_count = 0

    for key, value in ht.items():
        if value % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif value % 2 != 0 and odd_count != 0:
            return False
    else:
        return True

print(is_panlindrome_permutation(palin_perm))
print(is_panlindrome_permutation(not_palin_perm))