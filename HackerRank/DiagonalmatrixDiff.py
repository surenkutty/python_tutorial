def Diagonal(lst):
   
    frist=sum([lst[i][i] for i in range(len(lst))])
    second=sum([lst[i][len(lst)-1-i] for i in range(len(lst))])
    
    difference=abs(frist-second)
    
    
    
    return difference
    
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Diagonal(lst))