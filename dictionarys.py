# data to key and valuses mutable
# to use get update del keys(),valuse()
student={'name':'surend','age':20,'course':['cse','biomaths']}

print(student)
print(student['course'])
student['phone']=987739923
print(student.get('phon','notfound'))
student.update({'age':21})

del student['name']
print(student.items())

print(student.keys())
print(student.values())

for key in student:
    print(key)
for key,value in student.items():
    print(key,value)
