str = "Josue"

# Slice functions
print(str[::-1])

#recursion
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
    

print(string_reverse(str))