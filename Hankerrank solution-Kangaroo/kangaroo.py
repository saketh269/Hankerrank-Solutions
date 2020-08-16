#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
  k1=x1+v1
  k2=x2+v2
  if(k1==k2):
    return 1
  else:
    eq(k1,k2,v1,v2)
def eq(k1,k2,v1,v2):
    while(k1!=k2):
        k1=k1+v1
        k2=k2+v2
    return 1
        
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    if result==1:
      print("YES")
    else:
      print("NO")
