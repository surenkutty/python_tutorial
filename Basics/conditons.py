# and
# or
# not

user='admin'
logged_in=True

if user and logged_in:
    print("welcom Admin page")
else:
    print("Bad crides")
    
if user or logged_in:
    print("welcom Admin page")
else:
    print("Bad crides")

if not logged_in:
    print("welcom Admin page")
else:
    print("Bad crides")
    
# a=[1,2,3]
# b=[1,2,3]
# c=a
# print(id(a))
# print(id(b))
# print(a is c)


# none ,0,true,False,(),[],{} thats are all is empty so its flase
condition=''
if condition:
    print("this is condition True")
else:
    print("condition is False")
