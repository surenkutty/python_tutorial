class Signup(object):      #class clsname:
    def __init__(self,name,gender,email,password,) -> None:   #constructor
        self.name=name
        self.gender=gender
        self.email=email
        self.password=password

person1=Signup(name="surend",gender="male",email="surend@gmail",password="helloboy123")
print(person1.__dict__)