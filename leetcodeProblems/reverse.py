def reverse(x):
    INT_MIN = -2**31         # -2147483648
    INT_MAX = 2**31 - 1
    sign= -1 if x<0 else 1
    x=abs(x)
    rev=0
    while x!=0:
        pop=x%10
        x//=10
        rev=rev*10+pop
        if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
            return 0
    return sign*rev