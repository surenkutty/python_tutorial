import random
def qsort(arr):
    
    if len(arr)<=1:
        return arr
    pivot=random.choice(arr)    # or pivot =arr[len(arr)//2]
    left=[x for x in arr if x < pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x > pivot]
    
    return qsort(left)+middle+qsort(right)

if __name__=="__main__":
    arr=[2,5,1,4,3,9]
    ans=qsort(arr)
    print(ans)