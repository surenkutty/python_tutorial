def reversearray(arr):
    start=0                 #0
    end=len(arr)-1           #5-1=4
    while start<end:                 #0<4
        arr[start],arr[end]=arr[end],arr[start]   #0,4=4,0
        start+=1                                   #0+1=1
        end-=1                                      #4-1=3
    return arr

arr=[1,2,3,4,5]
print(reversearray(arr))