

import math
import os
import random
import re
import sys


def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    
    # Count positive, negative, and zero values
    for i in arr:
        if i < 0:
            negative += 1
        elif i > 0:
            positive += 1
        else:
            zero += 1
    
    length = len(arr)
    
    # Calculate ratios
    pos_ratio = positive / length
    neg_ratio = negative / length
    zero_ratio = zero / length
    print(pos_ratio)
    print(neg_ratio)
    print(zero_ratio)
    

    
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
