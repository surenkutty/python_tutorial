


# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    datas=[]
    
    for i in queries:
        datas.append(strings.count(i))
    return datas
            
    # Write your code here

if __name__ == '__main__':
    strings = ['ab','ab','abc']
    queries = ['ab','abc','bc']
    
    ans=matchingStrings(strings,queries)
    print(ans)

    
   
