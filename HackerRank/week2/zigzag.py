def zigzag(a,n):
    a.sort()
    mid=(n+1)//2
    a[mid],a[n-1]=a[n-1],a[mid]
    
    st=mid+1
    ed=n-2
    while st<=ed:
        a[st],a[ed]=a[ed],a[st]
        st+=1
        ed-=1
    print("".join(str(i) for i in a))
    
a=[4,3,7,8,6,2,1]
n=7
zigzag(a,n)


    
    