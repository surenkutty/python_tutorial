def replaceString(input1,input2,input3):
    n=len(input1)
    m=len(input2)
    print(input3)
    print(n)
    print(m)
    for i in range(n-m+1):
        if input1[i:i+m]==input2:
            return input1[:i]+input3+input1[i+m:]
    return False     
input1='welgo'
input2='we'
input3='come'

result=replaceString(input1,input2,input3)
print(result)