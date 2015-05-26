# -*- coding: utf-8 -*-
def prime(a,b):
    for i in range(a,b+1):
      if is_prime(i):
         print(i)

def is_prime(n):
    if n <= 1 :
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i=5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i=i+6
    return True

t = int(raw_input())

for i in range(t):
    str = raw_input()
    x,y = str.split(' ')
    x = long(x)
    y = long(y)
    prime(x,y)
