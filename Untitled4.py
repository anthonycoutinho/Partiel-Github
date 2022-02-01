#!/usr/bin/env python
# coding: utf-8

# In[10]:


#### 1. Création d'une fonction mathématique simple en Python
#### a) Implémenter la fonction polynomiale 
from math import*
def F(x):
    A=x**3-1,5*x**2-6*x+5
    return(A)


# In[11]:


F(5)


# In[3]:


#### b) Implémenter la fonction factorielle
def factorielle(n):
    if n== 0:
        return 1
    else:
        return n * factorielle(n-1)


# In[4]:


factorielle(5)


# In[5]:


#### c) Implémenter la suite de Fibonnaci
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("Entrez le nombre de termes:"))
print("Suite de Fibonacci en utilisant la recursion :")
for i in range(n):
    print(fibonacci(i))
    

