n=5

for i in range(n):
    for j in range(n):
        print("*", end="  ")
    print()

print("hello world")

for i in range(n):
    for j in range(i,n):
        print("*", end="  ")
    print()

'''
*  *  *  *  *
*  *  *  *
*  *  *  
*  *
*
'''