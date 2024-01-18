# prompt the user for input
sentence = input("Enter a sentence: ")

# convert the sentence to binary
binary = ''.join(format(ord(i), '08b') for i in sentence)

# convert the binary to inverted math
inverted_math = convert_to_inverted_math(binary)

# convert the inverted math back to binary
binary_back = convert_to_binary(inverted_math)

# convert the binary back to ascii
output = ''.join(chr(int(binary_back[i:i+8], 2)) for i in range(0, len(binary_back), 8))

# print the output
print(output)

def convert_to_inverted_math(binary):
    inverted_math = ""
    for i in binary:
        if i == "1":
            inverted_math += "i"
        elif i == "0":
            inverted_math += "π"
    return inverted_math
