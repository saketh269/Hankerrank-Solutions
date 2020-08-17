#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, q):
  a = [0]*n
  for i in q:
    a[i[0] - 1] += i[2]
    if i[1] != len(a):
      a[i[1]] -= i[2]
  b = 0
  c= 0
  print(a)
  for j in a:
    c+=j
    if c>b:
      b=c
  return b
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
