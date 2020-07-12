s1 = "Fairy tales"
s2 = "rail safety"

s1 = s1.strip().lower()
s2 = s2.strip().lower()

# Requires sorting
print(sorted(s1) == sorted(s2))

def is_anagram(s1, s2):
    
    if len(s1) != len(s2):
        return False
    
    ht = dict()

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            return False

    for i in ht:
        if ht[i] != 0:
            return False
        else:
            return True

print(is_anagram(s1, s2))
