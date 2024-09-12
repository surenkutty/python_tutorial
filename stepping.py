def displaySteppingNumbers(n,m):
    queue=[]
  
    for i in range(1,10):
        queue.append(i)
    while queue:
        stepNum=queue.pop(0)
        if stepNum>=n and stepNum<=m:
            print(stepNum,end='')
            if stepNum==0 or stepNum>m:
                continue
            lastDigit=stepNum%10
            stepNumA=stepNum*10+(lastDigit-1)
            stepNumB=stepNum*10+(lastDigit+1)
            
            if lastDigit==0:
                queue.append(stepNumB)
            elif lastDigit==9:
                queue.append(stepNumA)
            else:
                queue.append(stepNumA)
                queue.append(stepNumB)
n=0
m=100
print("stepping NUmbers b2w",n,"and",m,":",end='')
displaySteppingNumbers(n,m)
