#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    
    
    '''
    for i in a:
        if a.count(i)==1:
            result=i
            return result
    '''
     
     #or
    datas=[i for i in a if a.count(i)==1 ]
    for j in datas:
        return  j
    print(datas)
        
        
        
            
    
    
            
    # Write your code here

if __name__ == '__main__':
    a=[1,2,3,4,1,2,3]
    ans=lonelyinteger(a)
    print(ans)
