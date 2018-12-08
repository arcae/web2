#! /usr/bin/python3

import sys


print('Python version is: {}'.format(sys.version))
print('yes')




def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)


# In[ ]:


def fiboloop(n):
    a,b = 1,1
    for x in range(n):
        a,b = b,a+b
    return a


if __name__ == "__main__":
    print('======Now running the recursive algorithm for fibo=====')
    for i in range(1,19):
        print(fibo(i),end=' ')
    print('\n\n')
    print('======Now running the loop algorithm for fibo =======')
    for i in range(1,19):
        print(fiboloop(i),end=' ')
    print('\n\n')




