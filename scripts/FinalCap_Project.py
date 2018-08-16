
# coding: utf-8

# In[ ]:


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


# In[ ]:


for x in range(1,10):
    print(fibo(x))


# In[ ]:


for x in range(1,10):
    print(fiboloop(x))


# In[ ]:


def check_prime(n):
    for number in range(2,n):
        if n % number == 0:
            print(f'The number {n} is not prime')
            print(f'{n} can be divided by {number}')
            break
    else:
        print(f'The number {n} is prime!')
        
    


# In[ ]:


check_prime(977)


# In[ ]:


def list_primes(n):
    for x in range(2,n):
        prime = True
        for i in range(2,x):
            if x % i == 0:
                prime = False
        if prime:
            print(x)
        
    
    


# In[ ]:


check_prime(10)


# In[ ]:


list_primes(7)


# In[27]:


def change_return():
    cost = float(input('Please enter the total cost of purchase: '))
    print('The total cost of the purchase is ${}'.format(cost))
    money_given = float(input('Please enter the total money given: '))
    print('The total money given is ${}'.format(money_given))
    change_in_cents = int((money_given - cost)*100)
    print('The change in cents is {}'.format(change_in_cents))
    
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    
    while change_in_cents > 0:
        
        #print('Before IF')
        if change_in_cents > 25:
            quarters = int(change_in_cents / 25)
            #print('The number of quarters is {}'.format(quarters))
            change_in_cents = change_in_cents - quarters*25
            #print('change in cent is now {}'.format(change_in_cents))
            
        elif change_in_cents < 25 and change_in_cents >=10:
            #print('I am in the second block')
            dimes = int(change_in_cents / 10)
            change_in_cents = change_in_cents - dimes*10
            #print('The number of dimes is {}'.format(dimes))
            #print('change in cent is now {}'.format(change_in_cents))
            
        elif change_in_cents < 10 and change_in_cents >= 5:
            #print('I am in the third block')
            nickles = int(change_in_cents / 5)
            change_in_cents = change_in_cents - nickles*5
            #print('The number of nickles is {}'.format(nickles))
            #print('change in cent is now {}'.format(change_in_cents))
            
        elif change_in_cents < 5:
            #print('I am in the fourth block')
            pennies = int(change_in_cents / 1)
            change_in_cents = change_in_cents - pennies*1
            #print('The number of pennies is {}'.format(pennies))
            #print('change in cent is now {}'.format(change_in_cents))
            
            
    print('################################################')
    print('The number of quarters to be returned in change is {}'.format(quarters))
    print('The number of dimes to be returned in change is {}'.format(dimes))
    print('The number of nickles to be returned in change is {}'.format(nickles))
    print('The number of pennies to be returned in change is {}'.format(pennies))
              
          
 
            
            
        
   
     
            
        
    
    
   
        
    
   
    


# In[28]:


change_return()


# In[7]:


def bin_to_dec():
    bin_string = input('Please enter the binary digits: ')
    
    #print('The length of the binary string is {}'.format(len(bin_string)))
    
    dec = 0
    for i in range(0,len(bin_string)):
        dec = dec + int(bin_string[i])*2**(len(bin_string)-1-i)
    
    print(f'The decimal equivalent of {bin_string} is {dec}')
    
        
    
        
        


# In[8]:


bin_to_dec()


# In[4]:


def dec_to_binary():
    decimal = int(input('Please enter a decimal number: '))
    
    binary = []
    
    while decimal != 1:
        
        binary.append(decimal % 2)
        decimal =  int(decimal / 2)
        
    binary.append(decimal)
    
    binary = binary[::-1]
    
    #print('The binary equivalent is: {}'.format(binary))
    
    for i in range(len(binary)):
        print(binary[i],end='')
    
    #print(binary[::-1])
        
    


# In[5]:


dec_to_binary()


# In[1]:


def merge_divide(alist):
    import pdb
    print("Splitting  {}".format(alist))
    if len(alist) > 1:
        
        middle = len(alist)//2
        
        print('The middle is {}'.format(middle))

        llist = alist[:middle]
        rlist = alist[middle:]

        print('This is llist {}'.format(llist))
        print('This is rlist {}'.format(rlist))
        merge_divide(llist)
        merge_divide(rlist)
        #pdb.set_trace()
        
        i = 0
        m = 0
        k = 0
        
        while i < len(llist) and m < len(rlist):
            #pdb.set_trace()
            if llist[i] < rlist[m]:
                print('left half is less than right half')
                alist[k] = llist[i]
                i = i+1
                print('The value of i = {},  m = {} and k = {}'.format(i,m,k))
            else:
                print('left half is greater than right half')
                alist[k] = rlist[m]
                m = m +1
                print('The value of i = {},  m = {} and k = {}'.format(i,m,k))
            k = k + 1
            
            
        while i < len(llist):
            print('Here i is less than len(llist)')
            alist[k] = llist[i]
            i = i + 1
            k = k +1
            print('The value of i = {},  m = {} and k = {}'.format(i,m,k))
        while m < len(rlist):
            print('Here m is less than len(rlist)')
            alist[k] = rlist[m]
            m = m + 1
            k = k + 1
            print('The value of i = {},  m = {} and k = {}'.format(i,m,k))
            
    print("Merging {}".format(alist))
            
            
    
     
      


# In[4]:


alist = [116,-4,819,102]


# In[5]:


merge_divide(alist)


# In[55]:


3//2

