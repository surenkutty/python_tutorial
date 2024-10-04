lst=[2,2,3,4,5,2,3,5]
for i in range(1,len(lst)):
    d=[]
    for j in range(0,len(lst)):
        if lst[i]!=d:
            d.append(lst[i])
        else:
            j+=1