def pangram(s):
    s=s.lower()
    letters=set()
    
    for char in s:
        if char.isalpha():
            letters.add(char)
    return "pangram" if len(letters)==26 else "Not pangram"


s="The quick brown fox jumps over the lay dog"

ans=pangram(s)
print(ans)