arr=[1,2,4,7,5,6]  #0(n)space complexity     #0(n)timecomplexity
                    
T=8
l,r=0,len(arr)-1
h=1
while l<r:
    h=0
    act=arr[l]+arr[r]
    if act==T:
        
        print((l,r))
        break
    elif act<T:
        l+=1
    elif act>T:
        r-=1
 