import math
def sqr(x):
    l=0
    r=x
    while l<=r:
        m=(l+r)//2
        if m*m==x:
            return m
        if m*m<x:
            l=m+1
        else:
            r=m-1
    return m

print(sqr(200))

print(int(math.sqrt(200)))