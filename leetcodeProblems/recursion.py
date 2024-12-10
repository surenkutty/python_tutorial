def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=5
print(fact(n))


def fibonaci(n):
    if n<0:
        print("its cant conatine,try another input")
        
        
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    return fibonaci(n-1)+fibonaci(n-2)
print(fibonaci(5))
# 12,9,8,3