#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(a):
  c=0
  t=0
  for i in range(len(a)):
    while a[i]!=i+1:
      t=a[a[i]-1]
      a[a[i]-1]=a[i]
      a[i]=t
      c+=1
  return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
