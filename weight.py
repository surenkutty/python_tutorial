def weightMachine(N,weights,T):
    amount=0
    for i in weights:
        amount+=1
        if(i>T):
            amount+=1
    return amount
N=int(input())
weights=[]
for i  in range(N):
    weights.append(input(input()))
T=int(input())
print(weightMachine(N,weights,T))