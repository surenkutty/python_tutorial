"""
1.list
2.append()
3.insert()
4.sort()
5.index()
6.extend()
7.remove()
8.pop()
9.min()
10.max()
11.reverse()
12.enumurated()

"""


courses=['biology','maths','english','history']
print(courses[-1])
print(courses[3])

# -1 is last and negative
# print(courses[2:])  
# or print(courses[0:2])  
# ['biology', 'maths']

# append means add the item in last or add item
# courses.append('compsci')
# ['biology', 'maths', 'english', 'history', 'compsci']


# insert(index,values) to insert the DAta
# courses.insert(0,'art')
# ['art', 'biology', 'maths', 'english', 'history', 'compsci']


extra_courses=['Art','Education','Ecom']


# courses.insert(0,extra_courses)
# [['Art', 'Education', 'Ecom'], 'biology', 'maths', 'english', 'history', 'compsci'] iT conatain nested lists

# to using Extend keyword to cant contain nested lists
courses.extend(extra_courses)
courses.remove('Ecom')
# pop is remove or print -1 index or end element
popped=courses.pop()
print(popped)
# ['biology', 'maths', 'english', 'history', 'Art']




# courses.reverse()
# ['Art', 'history', 'english', 'maths', 'biology']

# sort is to order in assending order  key= sort() or sorted(variables)
courses.sort(reverse=True)
# ['maths', 'history', 'english', 'biology', 'Art']
# example
nums=[2,4,3,1,5]
print(min(nums))
print(max(nums))
print(sorted(nums))


print(courses.index('history'))
# True
print('maths' in courses)
for item in enumerate(courses,start=1):
    print(item)
'''
maths
history
english
biology
Art
'''
# enumurated key to disply the index
"""
(1, 'maths')
(2, 'history')
(3, 'english')
(4, 'biology')
(5, 'Art')
"""

datas=['name','email','pass','phone']
# join key word to remove list to the symbols detas
data_str='->'.join(datas)
new_list=data_str.split('>>')
print(datas)
print(new_list)