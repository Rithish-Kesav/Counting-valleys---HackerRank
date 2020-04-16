import math
import os
import random
import re
import sys


def countingValleys(n, s):
    count=0
    count1=0
    for i in s:
        if(i=='U'):
            count+=1
            if(count==0):
                count1+=1
        else:
            count-=1
    return count1        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
