input_str1 = "JeffHow"
input_str2 = "jeffHow"
input_str3 = "jeffhow"

def find_uppercase_linear(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    else:
        return "No Uppercase Character!"

def find_uppercase_recursive(input_str, index=0):
    if input_str[index].isupper():
        return input_str[index]
    if index == (len(input_str) - 1):
        return "No Uppercase Character!"
    return find_uppercase_recursive(input_str, index+1)

print(find_uppercase_linear(input_str1))
print(find_uppercase_linear(input_str2))
print(find_uppercase_linear(input_str3))

print(find_uppercase_recursive(input_str1))
print(find_uppercase_recursive(input_str2))
print(find_uppercase_recursive(input_str3))

