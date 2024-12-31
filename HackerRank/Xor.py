def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] != t[i]:
            res += '1'
        else:
            res += '0'  # Append '0' for matching bits (XOR rule)

    return res

# Input
s = input()
t = input()

# Output
print(strings_xor(s, t))
