input_str1 = "abc efg"
input_str2 = "JeffHow"

vowels = "aeiou"

def count_consonants_iterative(input_str):
    count = 0
    for i in input_str:
        if (i.lower() not in vowels) and (i.isalpha()):
            count += 1
    return count

def count_consonants_recursive(input_str):
    if input_str == "":
        return 0
    
    if (input_str[0].lower() not in vowels) and (input_str[0].isalpha()):
        return 1 + count_consonants_recursive(input_str[1:])
    else:
        return count_consonants_recursive(input_str[1:])

print(count_consonants_iterative(input_str2))
print(count_consonants_recursive(input_str2))