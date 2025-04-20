n=5
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print(False)  # False
    else:
        print(True)  # True
    print( f"prime is {i}")  # 2
