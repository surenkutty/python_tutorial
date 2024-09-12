
'''
row=int(input("enter the Row"))
column=int(input("enter the column"))
symbol=input("enter the Symbol")
for i in range(row):
    for j in range(column):
        print(symbol ,end=" ")
    print()
'''
'''
# n=int(input("enter n"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
'''

"""
list_friuts=['apple','orrange','mango']
for i in list_friuts:
    for j in i:
        print(j,end=" ")
    print()
        
"""
    
'''
row=11
for i in range(11):
    column=10
    for j in range(column):
        print("*", end=" ")
        j-=1
    i-=1
    print(' ')
'''
'''
list1=[10,11,12,13,14]
list2=[15,16,17,18]
result=[]
for i in list1:
    for j in list2:
        result.append(i+j)
      
print(result)
'''

# input1=input("enter the input 1:")
# input2=input("enter the input 2:")

list1=[2,3,4]
list2=[2,3,4]
print(list1)
print(list2)
for i in list1:
    for j in list2:
        if i==j:
            continue
        print(i,'*',j,'=',i*j)
        

name1='welgo'
name2='go'
x=list(name1)
y=list(name2)
for x in y:
    print( x)
