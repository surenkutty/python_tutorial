
# hash() -> check the hash values and its dynamic values


class HashMap:
    def __init__(self,size=10):
        self.size=size
        self.hashList=[None]*self.size
        
    def getIndex(self,key):
        return hash(key)% self.size
        
    def __setitem__(self,key,value):
        index=self.getIndex(key)
        
        if self.hashList[index] is None:
            self.hashList[index]=[[key,value]]
        else:
            self.hashList[index].append([key,value])
    def __getitem__(self,key):
        index=self.getIndex(key)
        if self.hashList[index] is not None:
            sublist=self.hashList[index]
            for pairs in sublist:
                if pairs[0]==key:
                    return pairs[1]
            # print(sublist)
                
        return "key is not Fount"
    def __delitem__(self,key):
        index=self.getIndex(key)
        if self.hashList[index] is not None:
            sublist=self.hashList[index]
            for i,pairs in enumerate(sublist):
                if pairs[0]==key:
                    del self.hashList[index][i]
                    return
        return "key is Not Found"
            
        
        
dic=HashMap()
print(dic.hashList)
dic["name"]="surend"
dic["age"]=21

print(dic.Get("age"))
del dic["age"]
print(dic.hashList)


        
