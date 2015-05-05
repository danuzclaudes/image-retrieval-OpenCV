#!/usr/bin/python
import math

a=[1,2,3]
b=[1,1,1]
[(x-y)**2 for x,y in zip(a,b)] # [0, 1, 4]
sum([(x-y)**2 for x,y in zip(a,b)]) # 5

print math.sqrt(sum([(x-y)**2 for x,y in zip(a,b)]))

