'''
a=[1,2,3,4,5,6,'AM']
print(a[:3])
print(a[3:])
print(a[2:-2])

'''
import os
def timeConvertion(s):
    period=s[-2:]
    hour=int(s[:2])
    
    if period=="AM":
        if hour==12:
            return "00"+s[2:-2]
        else:
            return s[:-2]
    else:
        if hour!=12:
            hour+=12
        return str(hour)+s[2:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConvertion(s)
    fptr.write(result + '\n')
    fptr.close()