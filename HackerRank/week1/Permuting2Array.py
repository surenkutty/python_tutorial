
def twoArrays(K,A,B):
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i]+B[i]<K:
            return "NO"
    return "YES"

def permutation(lst):
    if len(lst)==0:
        return []
    if len(lst)==1:
        return [lst]
    l=[]
    for i in range(len(lst)):
        m=lst[i]
        print("hello:",m)
        remLst=lst[:i]+lst[i+1:]
        for p in permutation(remLst):
            l.append([m]+p)
    return l
    


# Driver program to test above function
'''
data = list('123')
for p in permutation(data):
	print (p)'''

print(twoArrays(10, [2, 1, 3], [7, 8, 9]))  # YES
print(twoArrays(5, [1, 2, 2, 1], [3, 3, 3, 4]))  # NO
print(twoArrays(8, [4, 2, 6], [1, 5, 3]))  # YES
