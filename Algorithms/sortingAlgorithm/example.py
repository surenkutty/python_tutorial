
def bubble(arr):
    n=len(arr)-1
    for i in range(n):
        print(arr[i])
        
        for j in range(n-i):
            print("j->",j)
            
            if arr[j]>arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
               
        
    return arr
        
if __name__=="__main__":
    arr=[8,4,3,2,5,1]
    ans=bubble(arr)
    print(ans)

