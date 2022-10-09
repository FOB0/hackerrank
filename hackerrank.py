#!/usr/bin/env python
# coding: utf-8

# In[1]:


if __name__ == '__main__':
    print("Hello, World!")


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    elif n%2 == 0 and 2<=n<=5:
        print("Not Weird")
    elif n%2 == 0 and 6<=n<=20:
        print("Weird")
    else:
        print("Not Weird")


# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)


# In[ ]:


if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i**2)


# In[ ]:


def is_leap(year):
    leap = False
    if year%400==0:
        leap=True
    elif year%100==0:
        leap=False
    elif year%4==0:
        leap=True
    return leap
    

year = int(input())


# In[ ]:


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i+1,end="")


# In[ ]:


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mx = max(arr)
    sc = None

    for num in arr:
        if num == mx:
            pass
        elif sc == None:
            sc = num
        elif num > sc:
            sc = num

    print(sc)


# In[ ]:


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))


# In[ ]:


def split_and_join(line):
    split = line.split(" ")
    split = "-".join(split)
    return split

line = input()
result = split_and_join(line)
print(result)


# In[ ]:


def print_full_name(first, last):
    print("Hello " + first, last + "! You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# In[ ]:


def mutate_string(string, position, character):
    x = list(string)
    x[position] = character
    string = "".join(x)
    return string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# In[ ]:


if __name__ == '__main__':
    s = input()
    print(any(map(str.isalnum, s)))
    print(any(map(str.isalpha, s)))
    print(any(map(str.isdigit, s)))
    print(any(map(str.islower, s)))
    print(any(map(str.isupper, s)))


# In[ ]:


import textwrap

def wrap(string, max_width):
    for i in range(0,len(string)+1,max_width):
        x = string[i:i+max_width]
        if len(x) == max_width:
            print(x)
        else:
            return(x)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# In[ ]:


def merge_the_tools(string, k):
    x = []
    len_x = 0
    for item in string:
        len_x += 1
        if item not in x:
            x.append(item)
        if len_x == k:
            print (''.join(x))
            x = []
            len_x = 0
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# In[ ]:


N = int(input())
mset = set(map(int, input().split()))
M = int(input())
nset = set(map(int, input().split()))
mdef = mset.difference(nset)
ndef = nset.difference(mset)
output = mdef.union(ndef)
for i in sorted(list(output)):
    print(i)


# In[ ]:


N = int(input())

countries = set()

for i in range(N):
    countries.add(input())

print(len(countries))


# In[ ]:


x = int(input())
for i in range(x):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())

    # Athlete Sort in python - Hacker Rank Solution START   
    arr.sort(key = lambda x : x[k])
    for i in arr:
        print(*i,sep=' ')


# In[ ]:


s = input()
upper, lower,odd, even  = [], [], [], []

for char in s:
    if char.isnumeric():
        if int(char)%2 == 0:
            even.append(char)
        else:
            odd.append(char)
    else:
        if char.isupper():
            upper.append(char)
        else:
            lower.append(char)

print(''.join(sorted(lower))+''.join(sorted(upper))+''.join(sorted(odd))+''.join(sorted(even)))


# In[ ]:


cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    a = [0, 1]
    for i in range(2, n):
        a.append(a[i-1] + a[i-2])
    return(a[0:n])
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# In[ ]:


def wrapper(f):
    def fun(l):
        # complete the function
        f(['+91 ' + c[-10:-5] + ' ' + c[-5:] for c in l])
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


# In[ ]:


import numpy

def arrays(arr):
    return(numpy.array(arr[::-1], float))
arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# In[ ]:


import numpy
print(numpy.array(input().split(), int).reshape(3, 3))


# In[ ]:


import numpy

a,b,c=map(int,input().split())

lista1=[list(map(int,input().split())) for i in range(a)]
lista2=[list(map(int,input().split())) for i in range(b)]
a1=numpy.array(lista1)
a2=numpy.array(lista2)

print(numpy.concatenate((a1,a2),axis=0))


# In[ ]:


import numpy

N = tuple(map(int, input().split()))
print(numpy.zeros(N, int))
print(numpy.ones(N, int))


# In[ ]:


import numpy as np
np.set_printoptions(legacy='1.13')
n, m = list(map(int, input().split()))
print(np.eye(n, m, k=0))


# In[ ]:


import numpy

N, M = map(int, input().split())

A = numpy.array([list(map(int, input().split())) for n in range(N)])
B = numpy.array([list(map(int, input().split())) for n in range(N)])

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)


# In[ ]:


import numpy
numpy.set_printoptions(sign=' ')
a = numpy.array(input().split(),float)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))


# In[ ]:


import numpy

N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))


# In[ ]:


import numpy

N, M = map(int, input().split())
storage = numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(storage, axis=1), axis=0))


# In[ ]:


import numpy as np
n, m = list(map(int, input().split()))
a = np.array([list(map(int, input().split())) for _ in range(n)])
print(np.mean(a, axis=1))
print(np.var(a, axis=0))
print(round(np.std(a, axis=None), 11))


# In[ ]:


import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))


# In[ ]:


import numpy as np
A = np.array(input().split(), int)
B = np.array(input().split(), int)
print(np.inner(A,B), np.outer(A,B), sep='\n')


# In[ ]:


import numpy as np
poly = [float(x) for x in input().split()]
x = float(input())
print(np.polyval(poly, x))


# In[ ]:


import numpy
N = int(input())
A = numpy.array([input().split() for _ in range(N)], float)
print(round(numpy.linalg.det(A),2))


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    
    if x2 > x1 and v2 > v1:
        return "NO"
    else:
        if v2-v1 == 0:
            return 'NO'
        else:
            result = (x1-x2) % (v2-v1)
            if result == 0:
                return 'YES'
            else:
                return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    return 1 + (k * sum(int(x) for x in n) - 1) % 9

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[ ]:




