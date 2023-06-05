# reverse using slice()
input_str = 'srinivas'
print('srinivas =' [::-1])

# Reverse String using For Loop
def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1  # appending chars in reverse order
    return s1

input_str = 'srinivas'

if __name__ == "__main__":
    print('Reverse String using for loop =', reverse_for_loop(input_str))

    # Reverse a String using While Loop

def reverse_while_loop(s):
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1

input_str = 'srinivas'

if __name__ == "__main__":
    print('Reverse String using while loop =', reverse_while_loop(input_str))
elif __name__ != "__main__":
    print("reverse is not performed")
