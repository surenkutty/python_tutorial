class Employee:
    raise_amount=1.40
    def __init__(self,fname,lname,pay) -> None:
        self.fname=fname
        self.lname=lname
        self.email=fname+lname+'@gmail.com'
        self.pay=pay
        
    def fullname(self):
        return '{}{}'.format(self.fname,self.lname)
    def apply_rasie(self):
        self.pay=int(self.pay*self.raise_amount)
        
        

emp_1=Employee('hello','raj',10000)
print('{}'.format(emp_1.email))

emp_2=Employee('john','cena',2000)
print(emp_2.fullname())


emp_1.fname='surend'
emp_1.lname='kumar'
emp_1.email='surendkumar@gmail.com'
emp_1.pay=1000

emp_2.fname='hari'
emp_2.lname='suthan'
emp_2.email='harisuthan@gmail.com'
emp_2.pay=2000
print(emp_1.__dict__)
# print(emp_2.__dict__)
print(emp_1.apply_rasie())