#!/usr/bin/python3

import sys

def my_func():
    print('Hello World')


def check_prime(n):
    print('Python version is {}'.format(sys.version))
    for number in range(2,n):
        if n % number == 0:
            print(f'The number {n} is not prime')
            print(f'{n} can be divided by {number}')
            break
    else:
        print(f'The number {n} is a prime number')


'''
def check_prime(n):
    print('Python version is {}'.format(sys.version))
    for number in range(2,n):
        if n % number == 0:
            print(f'The number {n} is not prime')
            print(f'{n} can be divided by {number}')
            break
    	else:
            print(f'The number {n} is a pime number')
'''


if __name__ == "__main__":
   #check_prime(976)
    check_prime(971) 
    

