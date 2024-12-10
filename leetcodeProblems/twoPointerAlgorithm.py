 #0(n)space complexity     #0(n)timecomplexity
                     
def twopointer(arr,value):
    l=0
    r=len(arr)-1
    while l<r:
        act=arr[l]+arr[r]
        if act==value:
            return l,r
            continue
        if act<value:
            l+=1
        if act>value:
            
            r-=1
    return -1,-1 
if __name__=="__main__":
    arr=[1,2,4,7,5,6] 
    ans=twopointer(arr,9)
    print(ans)