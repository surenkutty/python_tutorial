def zero_end(arr):
    zero=[]
    nonzero=[]
    for i in range(len(arr)):
        if arr[i] !=0:
            nonzero.append(arr[i])
        else:
            zero.append(arr[i])
    com=nonzero+zero
    return com

# or
def move_zeros(arr):
    nonzero=[x for x in arr if x!=0]
    zero=[0]*(len(arr)-len(nonzero))
    return nonzero+zero



print(move_zeros([0, 4, 0, 5, 0, 1])) 
    