def hello(msg,name):
    return '{},{}'.format(msg,name)
 
print(hello('hello','surend'))

def students(*args, **kwargs):
    print(args)
    print(kwargs)
courses=['math','art']
info={'name':'surend','age':20}
    
# students(*courses,**info)


month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
def is_leep(year):
    return year %4 ==0 and(year %100 !=0 or year %400 ==0)
print(is_leep(2020))

def days_month(year,month):
    if not 1<= month <=12:
        return 'invaild month'
    if month==2 and is_leep(year):
        return 29
    return month_days[month]

print(days_month(2024,2))
        
        

# print(len(month_days))