#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, e, a, b, apples, oranges):
  start=s
  end=e
  noa=a
  noo=b
  ap=[]
  oo=[]
  c=0
  cp=0
  for j in apples:
    aa=a+j
    ap.append(aa)
  for j in oranges:
    bb=b+j
    oo.append(bb)
  for i in ap:
    if i in range(s,e+1):
      c=c+1
  print(c)
  for i in oo:
    if i in range(s,e+1):
      cp=cp+1
  print(cp)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
