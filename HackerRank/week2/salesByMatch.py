def sockMerchant(n, ar):
    
    sockSet = {} 
    
   
    for i in range(n):
        if ar[i] in sockSet:
            sockSet[ar[i]] += 1
        else:
            sockSet[ar[i]] = 1
            
    
    totalPairs = 0 
    for i in sockSet:
        if sockSet[i] != 0:
            totalPairs += (sockSet[i] // 2)
        
    return totalPairs 

if __name__=="__main__":
    n = int(input("Enter the lenght of list:"))
    ar = list(map(int, input("Enter the Input:").split()))
    print(sockMerchant(n, ar))