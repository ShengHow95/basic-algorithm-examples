input_str1 = "JeffHow"

def count_string_iterative(input_str):
    count = 0
    for i in input_str:
        count += 1
    return count

def count_string_recursive(input_str):
    if input_str == '':
        return 0
    return 1 + count_string_recursive(input_str[1:])

print(len(input_str1))
print(count_string_iterative(input_str1))
print(count_string_recursive(input_str1))

