def getMaxToys(n,arr,money):
    L,H=0,n-1
    while L<=H:
        if sum(arr[L:H+1])<=money:
            break
        elif arr[L] > arr[H]:
            L+=1
        else:
            H-=1
    return H-L+1
n=int(input("enter the no of array:"))
arr=list(map(int,input("enter the toy").split()))
money=int(input("enter the max amount"))
print(getMaxToys(n,arr,money))